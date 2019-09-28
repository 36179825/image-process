# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:39:32 2017

@author: Jasmine
"""

from skimage import io
import numpy as np
import math
import matplotlib.pyplot as plt

#read as color
lena = io.imread('lena512_8bit.bmp')

#io.imshow(lena)

h,w= lena.shape
lenak = np.zeros((h+2,w+2),dtype=np.uint8)
tan = 0
histogram = np.zeros(9)

for row in range(h):
    for col in range(w):
        lenak[row+1,col+1] = lena[row,col] 
h1,w1=lenak.shape
#邊界補0，每次跳64格
for row in range(1,h1-1,64):
    for col in range(1,w1-1,64):
        for r in range(64):#分割之後每個cell裡的所有格數全跑一次
            for c in range(64):#分成8*8個cell
                Gx = float(lenak[r+1, c] - lenak[r-1, c])
                Gy = float(lenak[r, c+1] - lenak[r, c-1])
                G = Gx*Gx + Gy*Gy
                Gxy = np.sqrt(G)
                if Gx==0 and Gy<0:#把分母為0的例外拉出來
                    tan = -90 
                elif Gx==0 and Gy>0:
                    tan = 90
                elif Gx==0 and Gy==0:
                    tan = 0
                else : tan = math.atan(Gy/Gx)#其餘的直接放進函式算
                if tan < 0:#調整。把tan負的+180變成正的
                    tan = tan + 180
                else : tan = tan
                h = int(tan // 20)#算出他的梯度屬於哪個範圍，在長度為9的array中，依照0~8把強度加上
                histogram[h] = histogram[h]+ Gxy
        bins = 9#print出直方圖
        plt.bar(np.arange(bins), histogram ,width = 1,align = 'center')
        plt.show()
    histogram = np.zeros(9)    
                