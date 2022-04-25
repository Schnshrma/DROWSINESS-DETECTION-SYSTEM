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
print("countThreshold is {}".format(serveConf["countThreshold"]))
countThreshold = serveConf["countThreshold"] # Threshold for detecting drowsiness of person
duration = serveConf["duration"] # seconds "alarm duration"
freq = serveConf["frequency"] # Hz
durationChange = serveConf["durationChange"] # Hz
frequencyChange = serveConf["frequencyChange"] # Hz
print(frequencyChange)

#duration = 0.1 # seconds "alarm duration"
#freq = 2000  # Hz

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

        if count>countThreshold:
            freq = freq-frequencyChange
            duration=duration+durationChange
            frame=put_red_rectangle(frame,face)
            frame=put_text(frame,face)
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        else:
            freq=serveConf["frequency"]
            duration = serveConf["duration"]
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

