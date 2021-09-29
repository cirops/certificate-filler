# Certificate Filler
This will fill your hundreds of event participation certificates without you having to do it by hand (at least until the signing).

## Usage
- Make sure you have python 3 installed on your machine: [Get Python](https://www.python.org/downloads/);
- Clone the project on your machine;
- Use your favorite command line terminal to go to the folder it was cloned, E.g.:
    - cd /home/user/certificate-filler (Linux);
    - cd C:\something\certificate-filler (Windows);
- Copy the background image of your certificate to the same folder in .png format (other formats probably work too, try it out and tell me);
- Copy a .csv file with a list of names, one per line, to the same folder;
- Run `python certificate-filler.py background-image.png list-of-participants.csv outputfolder` (make sure the output folder already exists);
- Check if everything worked by going to the output folder and opening the files!;
- Optionally, you can change the font type, size and text alignment by changing the following lines:
```
title_font = ImageFont.truetype("FreeSansBold.ttf", 28, encoding="unic")
```
and
```
image_editable.text((W/2-w ,355), title_text, (0, 0, 0), font=title_font)
```
, I might make those parameters later, we'll see;