# -*- coding: utf-8 -*-

"""
Created on Tue Dec 19 12:07:31 2017

@author: Gillian
"""

print("### Starting shard_counter.py ###")
from PIL import Image
import numpy as np
from pylab import imshow, show
import mahotas as mh
import scipy
import cv2

    #Reading Image
print('Reading Image...')
folder = "C:\\Users\\Gillian\\Documents\\School\\Dr. Dove's Microgravity Lab\\STRATA\\IMGS\\"
fname  = folder + '443_B2.jpg'
img    = Image.open(fname)
print img.size

    #Re-filtering image or raising sigma value yields more general 
    #and accruate shard regions, while sacrificing run time
img = mh.gaussian_filter(img, 20)
img = (img > img.mean())
imshow(img)
show()

    #Count how many Gaussian shapes were identified
labeled, blue_shard  = mh.label(img)
print('Found {} blue shards.'.format(blue_shard))
imshow(labeled)
show()