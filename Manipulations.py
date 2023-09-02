import cv2
import random
img = cv2.imread('assets/gitti.png',-1)

tag = img[90:120, 100:150]
img[50:80, 100:150] = tag

cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows