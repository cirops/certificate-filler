import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
from os import path
import csv

args = sys.argv[1:]

if (len(args) != 2):
    print("Usage: python certificate-email-sender.py list-of-participants.csv certificatefolder")
    quit()

participants_csv_path = args[0]
certificate_folder_path = args[1]

if(not path.exists(participants_csv_path)):
    print("file '" + participants_csv_path + "' does not exist.")
    quit()

if(not path.exists(certificate_folder_path)):
    print("folder '" + certificate_folder_path + "' does not exist.")
    quit()

# The mail addresses and password
sender_address = 'your@gmail.com'
sender_pass = 'addyourpasswordhere'

with open(participants_csv_path, 'r', newline='\n', encoding='latin-1') as csvfile:
    participantes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in participantes:
        receiver_name=row[0]
        receiver_address = row[1]

        mail_content = '''Hello, {participant_name}
        This is a template e-mail you should change this to whatever you want.
        Kind regards.'''.format(participant_name=receiver_name)

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Participation in an event at our institution'   #The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = certificate_folder_path + '/' + receiver_name + '.pdf'
        if(not path.exists(attach_file_name)):
            print("file " + attach_file_name + " does not exist. Exiting.")
            quit()

        attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        payload.add_header('Content-Disposition', 'attachment', filename=receiver_name + ".pdf")
        message.attach(payload)
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent to {participant_name} ({participant_email})'.format(participant_name=receiver_name, participant_email=receiver_address))