# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:49:57 2017

@author: Jasmine
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt

#read as color
pen = io.imread('pen.bmp')
h,w = pen.shape

io.imshow(pen)
io.show()

th = int(input('plz input a number:'))

grey = np.zeros((h,w),dtype=np.uint8)

for row in range(h):
    for col in range(w):
        if int(pen[row,col]) > th:
           pen[row,col] = 255
           grey[row,col] = pen[row,col]
        else:
           pen[row,col] = 0
           grey[row,col] = pen[row,col]


#grey value= 255, if grey > th
#grey value= 0, else.

io.imshow(grey)
io.show()