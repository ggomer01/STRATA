# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:42:47 2017
@author: Gillian
bar_remover.py
This program is meant to crop out the metal bar in STRATA images.
"""

print("### Starting bar_remover.py ###")
import sys
from scipy import misc
from skimage import io
import numpy as np
from PIL import Image
from PIL import ImageChops

    #Reading Image
print('Reading Image...')
folder = "C:\\Users\\Gillian\\Documents\\School\\Dr. Dove's Microgravity Lab\\STRATA\\IMGS\\"
fname  = folder + 'iss047e100443.jpg'
img    = Image.open(fname)

    #Rotate image so the metal bar is horizontal
img2   = img.rotate(0.70, expand = True)
#img2.save(folder + "img2_1.jpg")

    # Keep image portion above bar: rotate back to normal and recrop black space
img3   = img2.crop((0, 0, 8249, 2410))
img3   = img3.rotate(-0.7, expand = True)
img3   = img3.crop((30, 101, 8206, 2355))
#img3.save(folder + "img3_2.jpg")

    #Keep image portion below bar: rotate back to normal and recrop black space
img4   = img2.crop((0, 2823, 8249, 4522))
img4   = img4.rotate(-0.7, expand = True)
img4   = img4.crop((60, 109, 8249, 1693))
#img4.save(folder + "img4_2.jpg")

    #Retrieve sizes of both image portions
width3, height3 = img3.size
width4, height4 = img4.size

    #Find new image dimensions when portions are concatenated vertically
height = height3 + height4
width  = max(width3, width4)

    #Paste both portions into new, empty image of correct dimensions
result = Image.new("RGB", (width, height))
result.paste(img3, (0, 0))
result.paste(img4, (0, height3))
result.save(folder + "new_img3.jpg")
