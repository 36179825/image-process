# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:47:06 2017

@author: Jasmine
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt

#read as color
lena = io.imread('lena512_8bit.bmp')

io.imshow(lena)

h,w= lena.shape

low_pass_lena = lena.copy()

count = 0

#while count < 5 :
#    for row in range(1,h-1):
#        for col in range(1,w-1):
#            low_pass_lena[row,col] = sum(low_pass_lena[row-1:row+2,col-1:col+2])//9

#    plt.figure()
#    io.imshow(low_pass_lena)
#    io.show()
    
#    count = count + 1

A = [[1,2,1],[2,4,2],[1,2,1]]

while count < 8 :
    for row in range(1,h-1):
        for col in range(1,w-1):
            B = low_pass_lena[row-1:row+2,col-1:col+2];
            low_pass_lena[row,col] = sum(B * A )//16
     
    plt.figure()
    io.imshow(low_pass_lena)
    io.show()
    
    count = count + 1