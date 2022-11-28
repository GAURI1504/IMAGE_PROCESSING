# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:41:45 2021

@author: gauri
"""

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/gauri/Desktop/python codes/Example Images-20210701T101224Z-001/Example Images/Home.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r,g,b=cv2.split(img)
R = cv2.equalizeHist(r);
G = cv2.equalizeHist(g);
B = cv2.equalizeHist(b);
imgm=cv2.merge((R,G,B))

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original')
print(img.shape)
plt.subplot(1,2,2)
plt.imshow(imgm)
plt.title('Equlize')