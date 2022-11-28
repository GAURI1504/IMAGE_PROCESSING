# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:25:45 2021

@author: gauri
"""

import cv2
import matplotlib.pyplot as plt
img1=cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/1.jpg')
img2=cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/2.jpg')
sub=cv2.subtract(img2, img1)

plt.figure()
plt.subplot(1,3,1)
plt.imshow(img1)
plt.title('Original')
plt.subplot(1,3,2)
plt.imshow(img2)
plt.title('Background')
plt.subplot(1,3,3)
plt.imshow(sub,cmap='gray')
plt.title('Substracted')