import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1*mk1-6aYaf_Bes1E3Imhc0A.jpeg',-1)
cv2.imshow('image',img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
