import numpy as np
import cv2

img = cv2.imread('assets/CSGO.png',0)
man = cv2.imread('assets/man.png',0)
m416 = cv2.imread('assets/m416.png',0)
chick = cv2.imread('assets/chick.png',0)
siteB = cv2.imread('assets/siteB.png',0)

objects = [man,siteB,chick,m416]

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
for method in methods:
    color_img = cv2.imread('assets/CSGO.png')
    img2 = img.copy()
    for obj in objects:
        result = cv2.matchTemplate(img,obj,method)
        h,w = obj.shape
        min_val , max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        cv2.rectangle(color_img,location,(location[0]+w,location[1]+h), (255,0,0), 2)
    cv2.imshow('Match',color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    