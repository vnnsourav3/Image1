# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:07:12 2020

@author: Sourav
"""#Import required Image library
 
import cv2 
import os
from pil import Image,ImageFilter

im = Image.open('G:\chk2.jpg')

#im.show()
cropped = im.crop((472,147,703,241))
gaussImage = cropped.filter(ImageFilter.GaussianBlur(20))
im.paste(gaussImage,(472,147,703,241))

im.save('G:\masked1.jpg')

    
# Reading an image in default mode 
image = cv2.imread('G:\masked1.jpg') 
directory = r'G:\Chequemasking' 
os.chdir(directory)
print(os.listdir(directory))
# font 
font = cv2.FONT_HERSHEY_PLAIN
org = (472,220) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (40, 46, 43) 
  
# Line thickness of 2 px 
thickness = 1
   
# Using cv2.putText() method 
image = cv2.putText(image, 'MASKED BY FROST_BANK', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
   
# Displaying the image 
cv2.imwrite('showmepls.jpg',image)  