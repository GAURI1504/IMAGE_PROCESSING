# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:27:41 2021

@author: gauri
"""

import cv2 #impoert library
import numpy as np# for creating array
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001\Example Images/lowcontrast.png',0)
equ = cv2.equalizeHist(img);
plt.figure()
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('Orignal')
plt.subplot(2,2,2)
plt.hist(img.ravel(),256,[0,256]);
plt.title('Histogram');
plt.subplot(2,2,3)
plt.imshow(equ,cmap='gray');
plt.title('Equilize Image');
plt.subplot(2,2,4)
plt.hist(equ.ravel(),256,[0,256]);
plt.title('Equilize Histogram');
plt.show()