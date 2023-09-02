import cv2
import mediapipe as mp
import time
from handTrackingModule import handDetector

# # WITHOUT MODULE
# cap = cv2.VideoCapture(0)

# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpdraw = mp.solutions.drawing_utils
# ptime = 0
# ctime = 0
# while True:
#     ret, frame = cap.read()
#     frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     results = hands.process(frameRGB)
#     # print(results.multi_hand_landmarks)
#     if (results.multi_hand_landmarks):
#         for handLMS in results.multi_hand_landmarks:
#             for id,lm in enumerate(handLMS.landmark):
#                 h,w,c = frame.shape
#                 cx,cy = int(lm.x*w), int(lm.y*h)
#                 if id ==4:
#                     cv2.circle(frame, (cx,cy), 10, (255,0,255), -1)
#             mpdraw.draw_landmarks(frame,handLMS, mpHands.HAND_CONNECTIONS)
#     ctime = time.time()
#     fps = 1/(ctime-ptime)
#     ptime = ctime

#     cv2.putText(frame,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)

#     cv2.imshow("frame",frame) 
#     if cv2.waitKey(1) == ord('q'):
#         break

    
    
# cap.release()
# cv2.destroyAllWindows()




# #  WITH MODULE
# ptime = 0
# ctime = 0
# cap = cv2.VideoCapture(0)
# detector = handDetector()
# while True:
#     ret, frame = cap.read()
#     frame = detector.findHands(frame)
#     lmList = detector.findPosition(frame)
#     ctime = time.time()
#     fps = 1/(ctime-ptime)
#     ptime = ctime
#     cv2.putText(frame,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)

#     cv2.imshow("frame",frame) 
#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()