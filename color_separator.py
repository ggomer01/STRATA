# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:29:22 2017

@author: Seamus Anderson

color_analyzer.py

This program is meant to identify various colors in a STRATA image.
"""

print("### Starting color_separator.py ###")
import sys
from scipy import misc
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


    #Reading Image
print('Reading Image...')
folder = 'C:\\Users\\Seamus\\Desktop\\Research\\Colwell-Dove\\STRATA\\IMGS\\'
fname  = folder + 'IMG_1.jpg'

    #Printing Image Shape
img = io.imread(fname)
print('Image shape = ', img.shape)

    #Making an image of the STDev in the RGB channels
img_std = np.std(img, axis=2)       #img_std.shape = (4415, 8192)
fname   = folder + 'IMG_STDV.jpg'
misc.imsave(fname, img_std)
    #Making an image of the Avg across RGB channels
img_avg = np.mean(img, axis=2)
fname   = folder + 'IMG_AVG.jpg'
misc.imsave(fname, img_avg)
    #Making an image of the sum across RGB channels
img_sum = np.sum(img, axis=2)
fname   = folder + 'IMG_SUM.jpg'
misc.imsave(fname, img_sum)

    #Averaging the columns and rows and fitting parameters
img_avg_x = np.mean(img_avg, axis=0)
img_avg_y = np.mean(img_avg, axis=1)
x = np.arange(len(img_avg_x))
y = np.arange(len(img_avg_y))

x_fit = np.poly1d(np.polyfit(x, img_avg_x, 2))
y_fit = np.poly1d(np.polyfit(y, img_avg_y, 3))

    #Normalizing the image
x_norm = img

x_norm = np.multiply( img[:]
fname = folder + 'x_norm.jpg'
misc.imsave(fname, x_norm)



    #Making a binary mask  from deviation image(0 is bad, 1 is good)
img_std = np.where(img_std < 20, 0, 1)

RGB     = np.array(['R', 'G', 'B'])
new_img = img


    #Replacing non max with zero in each channel 
for i in range(3):
        #Eliminating RGB non maximums
        #If pixel in one channel is less than same pixel in other channels, set to 0, otherwise leave it be
    new_img[:,:,i] = np.where(img[:,:,i] < img[:,:,(i+1)%3], 0, img[:,:,i])  
    new_img[:,:,i] = np.where(img[:,:,i] < img[:,:,(i+2)%3], 0, img[:,:,i])
    
        #Eliminating bad pixels via std thresholding
    new_img[:,:,i] = np.multiply(new_img[:,:,i], img_std.astype(dtype="uint8"))
        
        #Saving processed img
    fname = folder + 'IMG_' + RGB[i] + '2.jpg'
    misc.imsave(fname, new_img[:,:,i])


    #PLotting 
plt.title('Average Pixel value across x')
plt.xlabel('Pixel Column Position (x axis Left->Right)')
plt.ylabel('Average value (0-255)')
plt.plot(x, x_fit(x), color='yellow')
plt.plot(x, img_avg_x, color='black')
fname = folder + 'X_Average_Pixel_value.jpg'
plt.savefig(fname)
plt.clf()

plt.title('Average Pixel value across y')
plt.xlabel('Pixel Row Position (y axis (Up->Down))')
plt.ylabel('Average value (0-255)')
plt.plot(y, y_fit(y))
plt.plot(y, img_avg_y)
fname = folder + 'Y_Average Pixel value.jpg'
plt.savefig(fname)
plt.clf()

plt.title('Average Pixel value across x')
plt.xlabel('Pixel Column Position (x axis (Left->Right))')
plt.ylabel('Average value (0-255)')
plt.plot(x, np.mean(img[:,:,0], axis=0), color='red',   label="Red")
plt.plot(x, np.mean(img[:,:,1], axis=0), color='green', label="Green")
plt.plot(x, np.mean(img[:,:,2], axis=0), color='blue',  label="Blue")
plt.plot(x, img_avg_x,                   color='black', label="Total Avg")
plt.legend(loc='upperleft')
fname = folder + 'RGB_column_avg.jpg'
plt.savefig(fname)

print("Saved!")

print("### Ending color_separator.py ###")


