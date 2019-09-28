# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:41:58 2017

@author: Jasmine
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt

#read as color
lena = io.imread('lena512_24bit.bmp')

#io.imshow(lena)

h,w,depth= lena.shape

bin2 = np.empty(255, dtype = int)
bins = 255

for row in range(h):
    for col in range(w):
            for d in range(depth):  
                bin = lena[row , col , d]
            bin2[bin] = bin2[bin] + 1
#B = bin2.tolist()
print(bin2)
#B = np.ravel(bin2)
#print(B) 
#h1_y,h1_x = np.histogram(255, bins = np.arange(0,255))
plt.bar(np.arange(bins), bin2 ,width = 1,align = 'center')
#plt.xticks(np.arange(bins))
#plt.hist(B, bins = np.arange(0,255,1))
plt.show()