import cv2#Video capturing
import os
from DrowsinessDetection import *
from detection import *
from draw import *

duration = 0.25 # seconds "alarm duration"
freq = 1500  # Hz

cap = cv2.VideoCapture(0)#for local access camera

#font = cv2.FONT_HERSHEY_TRIPLEX# for font of image 

count = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Frame", frame)
    
    faces = detector(gray)     #detect Faces in a frame

    for face in faces:

        landmarks = predictor(gray, face)   #detect landmarks in each face found one by one 
        
        if (checkDrowsiness(landmarks)):
            count = count+1
        else:
            count = 0

        if count>8:
            freq = freq+100
            duration=duration+0.05
            frame=put_red_rectangle(frame,face)
            frame=put_text(frame,face)
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        else:
            freq=1500
            duration = 0.25
            frame=put_rectangle(frame,face)
            

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
