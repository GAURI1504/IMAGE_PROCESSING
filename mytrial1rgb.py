# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:35:39 2021

@author: gauri
"""

import cv2  #library import
import matplotlib.pyplot as a #library import
img=cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/HAND.jpg')#image read
a.figure()
a.subplot(1,2,1)#for plotting multiple images we are using subplot command
#in subplot 1. ROW 2 . COL 3 . POS
a.imshow(img)#PLOT IS ALLOCATED TO FIRST IMAGE AND IT WILL BE DISPLAY 
a.title('Original')#TITLE OF IMAGE WILL BE GIVEN AS ORIGINAL
print(img.shape)#SIZE OF IMAGE WILL BE PRINTED
imgr=cv2.resize(img,(100,100), interpolation = cv2.INTER_AREA)#IMAGE WILL BE RESIZED AND WILL BECOME 100 X 100
a.subplot(1,2,2)# SIZE OF ROW AND COL WILL REMAIN SAME POS OF NEW IMAGE WILL BE CHANGED I.E 2
a.imshow(imgr)# IMAGE IS DISPLAYED WITH RESIZED VARIABLE IN THIS IMGR R STANDS FOR RESIZE VARIABLE 
a.title('Resize')# IMAGE IS DISPLAYED WITH TITLE RESIZE
cv2.imwrite('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/Rimg.jpg',imgr)# TO WRITE THE IMAGE ON THE OUTPUT SCREEN
r,g,b=cv2.split(img)#BY USING SPLIT COMMAND R,G,B WILL GET SPLITTED FROM THE IMAGE
a.figure()
a.subplot(2,2,1)#PLOT FOR R
a.imshow(r,cmap='gray')#CMAP MEANS COLOUR MAP NOTE: IT IS IS NOT REQUIRED WHEN COLOURED IMAGE IS USED
# R G B AR GRAY IMAGES
a.title('R')
a.subplot(2,2,2)#PLOT FOR G
a.imshow(g,cmap='gray')
a.title('G')
a.subplot(2,2,3)#PLOT FOR R
a.imshow(b,cmap='gray')
a.title('B')
imgm=cv2.merge((r,g,b))#TO MERGE
a.subplot(2,2,4)
a.imshow(imgm)
a.title('Merge')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lab=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
a.figure()
a.subplot(1,3,1)
a.imshow(gray,cmap='gray')
a.title('gray')
a.subplot(1,3,2)

a.imshow(lab)
a.title('LAB')
a.subplot(1,3,3)
a.imshow(hsv)
a.title('HSV')#IMAGE SATURATION VALUES
