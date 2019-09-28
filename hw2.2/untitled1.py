# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:47:44 2017

@author: Jasmine
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt

#read as color
flower = io.imread('flower_24bit.bmp')

h,w,depth = flower.shape

#>將一張彩圖show成3張圖，因此需要3個array接值，並且分別將array中所有值變成0，下面要保留channel時，
#只需要將要保留的channel塞入新的array中即可
r = np.zeros((h,w,depth),dtype=np.uint8)
g = np.zeros((h,w,depth),dtype=np.uint8)
b = np.zeros((h,w,depth),dtype=np.uint8)

#io.imshow(r)
#plt.figure()
#io.imshow(g)
#plt.figure()
#io.imshow(b)
#io.show()

for row in range(h):
    for col in range(w):
          r[row,col,0] = flower[row,col,0]#>此行保留紅色channel
          #r[row,col,2] = flower[row,col,2]>加上此行則在r中多保留藍色的channel
          g[row,col,1] = flower[row,col,1]
          b[row,col,2] = flower[row,col,2]

io.imshow(r)
plt.figure()
io.imshow(g)
plt.figure()
io.imshow(b)
io.show()