import cv2  #Video capturing
import os
# from DrowsinessDetection import *
from DrowsinessDetection2 import *
from detection import *
from draw import *
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

alarminfo = config_object["ALARMINFO"]
counters = config_object["COUNTERS"]

frameThreshold = int( counters["frameThreshold"])
duration = float ( alarminfo["duration"] ) # seconds "alarm duration"
freq = float(  alarminfo["freq"]  ) # Hz

cap = cv2.VideoCapture(0)#for local access camera

print(cap.get(cv2.CAP_PROP_FPS) )
cap.set(cv2.CAP_PROP_FPS, 15)
print("-------------")
print(cap.get(cv2.CAP_PROP_FPS) )
count = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)     #detect Faces in a frame

    for face in faces:

        landmarks = predictor(gray, face)   #detect landmarks in each face found one by one 
        
        if (checkDrowsiness(landmarks)):
            count = count+1
        else:
            count = 0

        if count>frameThreshold:
            freq = freq-50
            duration=duration+0.01
            frame=put_red_rectangle(frame,face)
            frame=put_text(frame,face)
            # print(count)
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        else:
            freq=2000
            duration = 0.1
            frame=put_rectangle(frame,face)
            

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


saveEyeBlinkingRatio()

