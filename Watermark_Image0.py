
from PIL import Image
#import os
photo=Image.open('C:/Users/Pratik/Desktop/de/123.png')


#photo.show()
logo1=Image.open('ieee.png')
logo2=Image.open('VIT.png')
photo_copy=photo.copy()
w=photo_copy.size[0]
h=photo_copy.size[1]

#print(w,h)
#print(logo2.width, logo2.height)
widthRatio  = int(w/logo2.width)
heightRatio = int(h/logo2.height)

newWidth    = int(widthRatio*logo2.width)
newHeight   = int(heightRatio*logo2.height)

logo2.thumbnail( (newWidth, newHeight), Image.ANTIALIAS)
position = ((photo_copy.width - logo2.width), (photo_copy.height - logo2.height))
#positio = ((photo_copy.width - logo1.width), (photo_copy.height - logo1.height) )
photo_copy.paste(logo2, position, logo2)
photo_copy.paste(logo1, positio, logo1)

photo_copy.show()

