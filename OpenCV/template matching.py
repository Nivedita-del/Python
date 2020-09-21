import cv2
import numpy as np
img = cv2.imread("1*mk1-6aYaf_Bes1E3Imhc0A (copy).jpg")
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread("Screenshot from 2020-05-02 21-03-59.png",0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
#TM_CCOEFF_NORMED is template matching
print(res)
threshold =0.999
loc = np.where(res>= threshold)
print(loc)
#if there are multiple number of matched template
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2) #initializing (original image, first point of rect ie top left corner, bottom right corner variable ,col,width

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()