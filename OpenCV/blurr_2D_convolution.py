import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Screenshot from 2020-04-25 22-41-14.png')

kenel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kenel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


