import sys
from PIL import Image, ImageFont, ImageDraw

args = sys.argv[1:]

if (len(args) != 3):
    print("Usage: python certificate-filler.py background-image.png list-of-participants.csv outputfolder")
    quit()

bg_image = Image.open(args[0])

print(bg_image)
title_font = ImageFont.truetype("FreeSansBold.ttf", 28, encoding="unic")

import csv
with open(args[1], 'r', newline='\n', encoding='latin-1') as csvfile:
    participantes = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in participantes:

        title_text = row[0]
        bg_image = Image.open(args[0])
        image_editable = ImageDraw.Draw(bg_image)
        W, H = image_editable.im.size
        w, h = image_editable.textsize(title_text)

        image_editable.text((W/2-w ,355), title_text, (0, 0, 0), font=title_font)


        im1 = bg_image.convert('RGB')
        im1.save(args[2] + "/" + row[0] + ".pdf")