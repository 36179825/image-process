# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:41:40 2017

@author: Jasmine
"""

from skimage import io
#import math
import numpy as np
import matplotlib.pyplot as plt

#read as color
lena = io.imread('lena512_8bit.bmp')

io.imshow(lena)

#lena = lena.astype(np.int32)

#lenaG = lena.copy()


h,w= lena.shape

lenaG = np.zeros((h+2,w+2),dtype=np.uint8)
lenaG1 = np.zeros((h,w),dtype=np.uint8)

plt.figure()
#io.imshow(lenaG)

Gx=[[-1,0,1],[-2,0,2],[-1,0,1]]
Gy=[[-1,-2,-1],[0,0,0],[1,2,1]]

for row in range(h):
    for col in range(w):
        lenaG[row+1,col+1] = lena[row,col] 
for row in range(1,h-1):
    for col in range(1,w-1):
        d=0
        e=0
        B = lenaG[row-1:row+2,col-1:col+2];
        Gx1 = Gx * B
        Gy1 = Gy * B
        Gx2 = Gx1.reshape(1,9)
        Gy2 = Gy1.reshape(1,9)
        for c in range(0,9):
            a = Gx2[0,c]
            d = a + d
            b = Gy2[0,c]
            e = b + e
        s = d*d + e*e
        ans = np.sqrt(s)
        lenaG1[row,col] = int(ans)
        

#lenaG = lenaG.astype(np.uint8)
     
plt.figure()
io.imshow(lenaG1)
io.show()