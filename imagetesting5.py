# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:07:12 2020

@author: Sourav
"""#Import required Image library

from PIL import Image, ImageFilter
im = Image.open('G:\chk2.jpg')
#im.show()
cropped = im.crop((472,147,703,241))
gaussImage = cropped.filter(ImageFilter.GaussianBlur(10))
im.paste(gaussImage,(472,147,703,241))
im.save('G:\masked.jpg')
