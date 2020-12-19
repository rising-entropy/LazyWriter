# sheet size is 2480 * 3508
# we have margins of 120 and 48

from PIL import Image
import os

img = Image.open("Canvas/sheet.png")
img.save("sheet.png")

print("Choose Your Font:")
print("1. Lamptey\n2. Alexandria\n3. Mersey")
print("Your Choice: ", end='')
choice = int(input())
if choice == 1:

    #open the file
    f = open('data.txt', 'r')
    data = f.read()
    xP = 120
    yP = 48
    data += " "
    for i in range(len(data)):
        try:
            if i == len(data) - 1:
                continue
            #open the image
            image = Image.open('sheet.png')
            #os.remove('sheet.png')
            if data[i] == " ":
                char = "LampteyFont/space.png"
            elif data[i] == ".":
                char = "LampteyFont/dot.png"
            elif data[i] == "~":
                char = "LampteyFont/tilde.png"
            elif data[i] == "/":
                char = "LampteyFont/fslash.png"
            elif data[i] == '\n':
                xP = 120
                yP += 120
                if yP > 3494:
                    break
                continue
            else:
                char = data[i]+".png"
                char = "LampteyFont/" + char
            img2 = Image.open(char)
            pos = ((xP), (yP))
            image.paste(img2, pos, img2)
            image.save("sheet.png")
            xP += 60
            if xP > 2360:
                xP = 120
                yP += 120
                if yP > 3460:
                    break
            if xP >= 2240:
                if data[i+1] == " " or data[i+1] == "\n" or data[i+1] == "'" or data[i+1] == "-":
                    continue
                else:
                    char = "LampteyFont/-.png"
                    img2 = Image.open(char)
                    pos = ((xP), (yP))
                    image.paste(img2, pos, img2)
                    image.save("sheet.png")
                    xP = 120
                    yP += 120
                    if yP > 3460:
                        break
        except:
            print("Invalid Character")
            break
    print("Image is now Complete.")

elif choice == 2:
    #open the file
    f = open('data.txt', 'r')
    data = f.read()
    xP = 120
    yP = 48
    data += " "
    for i in range(len(data)):
        try:
            if i == len(data) - 1:
                continue
            #open the image
            image = Image.open('sheet.png')
            #os.remove('sheet.png')
            if data[i] == " ":
                char = "AlexandriaFont/space.png"
            elif data[i] == ".":
                char = "AlexandriaFont/dot.png"
            elif data[i] == "~":
                char = "AlexandriaFont/tilde.png"
            elif data[i] == "/":
                char = "AlexandriaFont/fslash.png"
            elif data[i] == '\n':
                xP = 120
                yP += 120
                if yP > 3494:
                    break
                continue
            else:
                char = data[i]+".png"
                char = "AlexandriaFont/" + char
            img2 = Image.open(char)
            (x, y) = img2.size
            pos = ((xP), (yP))
            image.paste(img2, pos, img2)
            image.save("sheet.png")
            xP += x
            if xP > 2360:
                xP = 120
                yP += 120
                if yP > 3460:
                    break
            if xP >= 2240:
                if data[i+1] == " " or data[i+1] == "\n" or data[i+1] == "'" or data[i+1] == "-":
                    continue
                else:
                    char = "AlexandriaFont/-.png"
                    img2 = Image.open(char)
                    pos = ((xP), (yP))
                    image.paste(img2, pos, img2)
                    image.save("sheet.png")
                    xP = 120
                    yP += 120
                    if yP > 3460:
                        break
        except:
            print("Invalid Character")
            break
    print("Image is now Complete.")

elif choice == 3:
    #open the file
    f = open('data.txt', 'r')
    data = f.read()
    xP = 120
    yP = 48
    data += " "
    for i in range(len(data)):
        try:
            if i == len(data) - 1:
                continue
            #open the image
            image = Image.open('sheet.png')
            #os.remove('sheet.png')
            if data[i] == " ":
                char = "MerseyFont/space.png"
            elif data[i] == ".":
                char = "MerseyFont/dot.png"
            elif data[i] == "~":
                char = "MerseyFont/tilde.png"
            elif data[i] == "/":
                char = "MerseyFont/fslash.png"
            elif data[i] == '\n':
                xP = 120
                yP += 120
                if yP > 3494:
                    break
                continue
            else:
                char = data[i]+".png"
                char = "MerseyFont/" + char
            img2 = Image.open(char)
            (x, y) = img2.size
            pos = ((xP), (yP))
            image.paste(img2, pos, img2)
            image.save("sheet.png")
            xP += x
            if xP > 2360:
                xP = 120
                yP += 120
                if yP > 3460:
                    break
            if xP >= 2240:
                if data[i+1] == " " or data[i+1] == "\n" or data[i+1] == "'" or data[i+1] == "-":
                    continue
                else:
                    char = "MerseyFont/-.png"
                    img2 = Image.open(char)
                    pos = ((xP), (yP))
                    image.paste(img2, pos, img2)
                    image.save("sheet.png")
                    xP = 120
                    yP += 120
                    if yP > 3460:
                        break
        except:
            print("Invalid Character")
            break
    print("Image is now Complete.")

else:
    print("Invalid Choice.")

imgur = Image.open('sheet.png')
imgur.save('sheet.pdf')
print("PDF is Ready.")