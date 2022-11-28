# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:46:19 2021

@author: gauri
"""

import cv2#importing cv2 library
import matplotlib.pyplot as plt# importing matplot library for plotting
from skimage.filters import roberts, sobel, prewitt#roberts, sobel, prewitt are functions of sk image filter

img = cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/Home.jpg',0)
#image read (0) so that image is read on gray scale because edge dectection is done on gray scale images
# Canny
edge_canny = cv2.Canny(img,100,200)
#canny function is used along with cv2 and (100,200) is the size of page according to which edges will be detected
# Calcution of Sobel
edge_sobel = sobel(img)
# Prewitt Operator
edge_prewitt = prewitt(img)
#Robert
edge_roberts = roberts(img)

plt.subplot(4,2,1)#images will be shown on 4 row and 2 col 
plt.imshow(img,cmap='gray') 
plt.title('Orignal')
plt.subplot(4,2,2)
plt.imshow(edge_canny,cmap='gray')
plt.title('Canny')
plt.subplot(4,2,3)
plt.imshow(edge_sobel,cmap='gray')#these are all image model canny to roberts
plt.title('Sobel')
plt.subplot(4,2,4)
plt.imshow(edge_prewitt,cmap='gray')
plt.title('Prewitt')
plt.subplot(4,2,5)
plt.imshow(edge_roberts,cmap='gray')
plt.title('Roberts')
plt.show()#to show all the images in one go
# 1 space for image is empty because we have less images available right now