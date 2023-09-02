import cv2;

img = cv2.imread('assets\gitti.png', 1)
img = cv2.resize(img,(200,200))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_logo.png',img)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
