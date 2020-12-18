# sheet size is 2480 * 3508
# we have margins of 40 and 14

from PIL import Image
import os

img = Image.open("Canvas/sheet.png")
img.save("sheet.png")

print("Choose Your Font:")
print("1. Devang")
print("Your Choice: ", end='')
choice = int(input())
if choice == 1:

    #open the file
    f = open('data.txt', 'r')
    data = f.read()
    xP = 40
    yP = 14
    for i in data:
        try:
            #open the image
            image = Image.open('sheet.png')
            #os.remove('sheet.png')
            if i == " ":
                char = "DevangFont/space.png"
            elif i == ".":
                char = "DevangFont/dot.png"
            elif i == "~":
                char = "DevangFont/tilde.png"
            elif i == "/":
                char = "DevangFont/fslash.png"
            elif i == '\n':
                xP = 40
                yP += 120
                if yP > 3494:
                    break
                continue
            else:
                char = i+".png"
                char = "DevangFont/" + char
            img2 = Image.open(char)
            pos = ((xP), (yP))
            image.paste(img2, pos, img2)
            image.save("sheet.png")
            xP += 60
            if xP > 2440:
                xP = 40
                yP += 120
                if yP > 3494:
                    break

        except:
            print("Invalid Character")
    print("Image is now Complete.")
else:
    print("Invalid Choice.")