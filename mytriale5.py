# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:10:18 2021

@author: gauri
"""

import cv2#imprting cv2 library
import numpy as np# using numpy library for creating array
import matplotlib.pyplot as plt# for plotting

img = cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/j.png')
# for reading image
kernel = np.ones((5,5),np.uint8)# (5,5) means 5x5 matrix for image 
# this 5x5 matrix elements will be checked on the image
# Erosion
erosion = cv2.erode(img,kernel,iterations = 1)#kerent means structuring iterations = 1 means it will erode the pixel for ones and if we take 2 then it will erode the pixel for twice
# dilation
dilation = cv2.dilate(img,kernel,iterations = 5)# dialate means it will add the pixels
# opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)#morph is fuction used for openning and closing
#no need to give iterations in opening and closing
# closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)#morph is fuction used for openning and closing
#no need to give iterations in opening and closing

fig=plt.figure()
ax1=fig.add_subplot(3,2,1)
plt.imshow(img)
ax1.title.set_text('Orignal')
ax2=fig.add_subplot(3,2,2)
plt.imshow(erosion)
ax2.title.set_text('Erosion')
ax3=fig.add_subplot(3,2,3)
plt.imshow(dilation)
ax3.title.set_text('Dilation')# we can change plots acc to our needs
ax4=fig.add_subplot(3,2,4)
plt.imshow(opening)
ax4.title.set_text('Opening')
ax5=fig.add_subplot(3,2,5)
plt.imshow(closing)
ax5.title.set_text('Closing')
plt.show()
