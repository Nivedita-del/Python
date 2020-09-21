import cv2
import numpy as np
img = cv2.imread("1*mk1-6aYaf_Bes1E3Imhc0A.jpeg")
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

layer = gp[5]

cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
