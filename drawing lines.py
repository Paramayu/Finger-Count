import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (20,20),(width,height),(0,255,0), 10)
    img = cv2.line(img, (0,height),(width,0),(255,0,0), 5)
    img = cv2.rectangle(img,(0,0),(width,height), (255,255,128), 10)
    img = cv2.circle(img,(width//2,height//2), 50 , (250,118,30), -1)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img,"Hello", (40,200), font, 1,(0,0,0), 6 ,cv2.LINE_AA)
    cv2.imshow('frame',img)
    

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()