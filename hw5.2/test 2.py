# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:58:28 2017

@author: Jasmine
"""
from skimage import io
import numpy as np
import math
import matplotlib.pyplot as plt
Gx=1
Gy=4
histogram = np.zeros(9)
Gxy=1

if Gx==0 and Gy<0:#把分母為0的例外拉出來
    tan = -90 
elif Gx==0 and Gy>0:
    tan = 90
elif Gx==0 and Gy==0:
    tan = 0
else : 
    t = math.atan(float(Gy)/float(Gx))#其餘的直接放進函式算
    tan = math.degrees(t)
if tan < 0:#調整。把tan負的+180變成正的
    tan = tan + 180
else : tan = tan
        #print(tan)
        #print(Gxy)
h = int(tan // 20)#算出他的梯度屬於哪個範圍，在長度為9的array中，依照0~8把強度加上
histogram[h] = histogram[h]+ Gxy
bins = 9#print出直方圖
plt.bar(np.arange(bins), histogram ,width = 1,align = 'center')
plt.show()

print(tan)