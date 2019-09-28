# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:47:29 2017

@author: Jasmine
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt

lena = io.imread('lena_salt_ pepper.bmp')

io.imshow(lena)

lenaa = lena.copy()

h,w= lena.shape

for row in range(1,h-1):
    for col in range(1,w-1):
        A = lenaa[row-1:row+2,col-1:col+2]
        B = A.reshape(1,9)
        B.sort()
        #print(B)
        lenaa[row,col] = B[0,4]
#plt.figure()
#io.imshow(lena)
plt.figure()
io.imshow(lenaa)
io.show()