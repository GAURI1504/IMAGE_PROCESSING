# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:14:20 2021

@author: gauri
"""

import cv2# import files
import numpy as np#for creating ARRAY
import matplotlib.pyplot as plt
img=cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001\Example Images/cameramannoise.jpg')
imag = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#CONVERTING IMAGE INTO RGB
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) # COVERT IMAGE INTO GRAY
# apply the 3x3 median filter on the image
blur0 = cv2.medianBlur(img, 3)
# Gaussian
blur1 = cv2.GaussianBlur(img,(5,5),0)
# Bilateral
blur2 = cv2.bilateralFilter(img,9,75,75)
#Average
kernel = np.ones((5,5),np.float32)/25
blur3 = cv2.filter2D(img,-1,kernel)

plt.figure()
plt.subplot(2,3,1)
plt.imshow(imag,cmap='gray')
plt.title('Original')
plt.subplot(2,3,2)
plt.imshow(blur0,cmap='gray')
plt.title('Median')
plt.subplot(2,3,3)
plt.imshow(blur1,cmap='gray')
plt.title('Gaussian')
plt.subplot(2,3,4)
plt.imshow(blur2,cmap='gray')
plt.title('Bilateral')
plt.subplot(2,3,5)
plt.imshow(blur3,cmap='gray')
plt.title('Average')