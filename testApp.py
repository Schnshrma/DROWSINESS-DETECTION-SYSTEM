from configparser import ConfigParser
import cv2#Video capturing
import os
# from DrowsinessDetection import *
from DrowsinessDetection2 import *
from detection import *
from draw import *
import pickle

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the count, duration and frequency from config file
serveConf = config_object["SERVERCONFIG"]
print("Password is {}".format(serveConf["count"]))
count = serveConf["count"] # Threshold for detecting drowsiness of person
duration = serveConf["duration"] # seconds "alarm duration"
freq = serveConf["frequency"] # Hz
print(count)

#duration = 0.1 # seconds "alarm duration"
#freq = 2000  # Hz

cap = cv2.VideoCapture(0)#for local access camera

#font = cv2.FONT_HERSHEY_TRIPLEX# for font of image 


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

        if count>10:
            freq = freq-50
            duration=duration+0.01
            frame=put_red_rectangle(frame,face)
            frame=put_text(frame,face)
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

# eyeBlinkingRatio = getBlinkingRatios()

# with open("eyeBlinkingData2", "wb") as fp:   #Pickling
#     pickle.dump(eyeBlinkingRatio, fp)

# mouthRatios = getMouthRatios()

# with open("mouthData2", "wb") as fp:   #Pickling
#     pickle.dump(mouthRatios, fp)

