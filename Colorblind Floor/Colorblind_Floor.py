from PIL import ImageGrab
im = ImageGrab.grabclipboard()

#? Load Image From Clipboard
try:pix = im.load()
except:print('First You Have To Printscreen The Stream!');input()
sizeOfImage = im.size
print('Your Resolution:',sizeOfImage) #(1920, 1040)


#? find the main colour (resolution used (1920, 1040))
colourToFind = pix[1000,230]


#? iterate over whole image and find the colour
for i in range(sizeOfImage[0]):
    for p in range(sizeOfImage[1]):
        if pix[i,p] == colourToFind:
            found = True
            pix[i,p] = (255, 0, 0)
print('Correct Floor Found?', found)
if found:print('Check OUTPUT_IMAGE.png')

im.save('OUTPUT_IMAGE.png')  # Save the modified

input()