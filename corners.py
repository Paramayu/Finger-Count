import numpy as np
import cv2

cam = cv2.VideoCapture(0)


def display(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(grey, 100, 0.5, 10)
    corners = np.int0(corners)
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(img,(x,y),3,(255,0,0), -1)
    for i in range(len(corners)):
            for j in range(i+1, len(corners)):
                corner1 = tuple(corners[i][0])
                corner2 = tuple(corners[j][0])
                color = tuple(map(lambda x:int(x),np.random.randint(0,255,size=3)))
                cv2.line(img,corner1,corner2,color,1)

    cv2.imshow('frame', img)
    
while True:
    ret,frame = cam.read()
    display(frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()