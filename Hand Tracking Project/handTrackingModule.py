import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False, maxHands=2,model_complexity=1,detection_confidence=0.5,tracking_confidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.model_complexity,self.detection_confidence,self.tracking_confidence)
        self.mpdraw = mp.solutions.drawing_utils
    
    def findHands(self,frame,draw = True):

        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frameRGB)
        # print(results.multi_hand_landmarks)
        if (self.results.multi_hand_landmarks):
            for handLMS in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(frame,handLMS, self.mpHands.HAND_CONNECTIONS)
        return frame

    def findPosition(self,frame,handNo=0,draw = True):

        lmList = []
        if (self.results.multi_hand_landmarks):
            myHand = self.results.multi_hand_landmarks[handNo]

            for id,lm in enumerate(myHand.landmark):
                h,w,c = frame.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                # print(id,cx,cy)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(frame, (cx,cy), 5, (255,0,255), -1)

        return lmList
    

    
    

def main():
    ptime = 0
    ctime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        ret, frame = cap.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame)
        if len(lmList) > 4:
            print(lmList[4])
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv2.putText(frame,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)

        cv2.imshow("frame",frame) 
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()