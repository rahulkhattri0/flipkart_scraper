import cv2 as cv
import mediapipe as mp
import time

cap=cv.VideoCapture(0)
mphands=mp.solutions.hands
hands=mphands.Hands()
mpDraw=mp.solutions.drawing_utils
mpface=mp.solutions.face_detection
facedetection=mpface.FaceDetection()
ptime=0
ctime=0
while True:
    ret,frame=cap.read()
    imgRgb= cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=hands.process(imgRgb)
    results2=facedetection.process(imgRgb)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,handLms,mphands.HAND_CONNECTIONS)
    if results2.detections:
        for id,detection in enumerate(results2.detections):
            mpDraw.draw_detection(frame,detection)
            # cv.cvtColor(results.detections,cv.COLOR_BGR2GRAY)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(frame,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow('my vid',frame)
    if cv.waitKey(10) & 0xFF==ord('q'):
        break
    
