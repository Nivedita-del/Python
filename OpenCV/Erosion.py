import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Screenshot from 2020-04-26 12-13-26.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(erosion),plt.title('Output')

plt.show()
