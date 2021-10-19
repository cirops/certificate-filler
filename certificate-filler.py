import sys
import img2pdf
from os import path, mkdir, remove
from PIL import Image, ImageFont, ImageDraw

args = sys.argv[1:]

if (len(args) != 3):
    print("Usage: python certificate-filler.py background-image.png list-of-participants.csv outputfolder")
    quit()

bg_image_path = args[0]
participants_csv_path = args[1]
output_folder_path = args[2]

if(not path.exists(bg_image_path)):
    print("file '" + bg_image_path + "' does not exist.")
    quit()

if(not path.exists(participants_csv_path)):
    print("file '" + participants_csv_path + "' does not exist.")
    quit()

if(not path.exists(output_folder_path)):
    mkdir(output_folder_path)

bg_image = Image.open(bg_image_path)

title_font = ImageFont.truetype("FreeSansBold.ttf", 32, encoding="unic")

import csv
with open(participants_csv_path, 'r', newline='\n', encoding='latin-1') as csvfile:
    participantes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in participantes:

        title_text = row[0]
        bg_image = Image.open(bg_image_path)
        image_editable = ImageDraw.Draw(bg_image)
        W, H = image_editable.im.size
        w, h = image_editable.textsize(title_text)

        image_editable.text((W/2-w-40 ,355), title_text, (0, 0, 0), font=title_font)


        im1 = bg_image.convert('RGB')   
        filename = output_folder_path + "/" + row[0]
        im1.save(filename + ".png",quality=100, optimize=False)
        
        with open(filename + ".pdf","wb") as f:
            f.write(img2pdf.convert(filename + ".png"))
            remove(filename + ".png")