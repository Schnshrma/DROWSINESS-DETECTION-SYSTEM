import cv2  #Video capturing
import os
from drowsinessDetection import *
from detection import *
from draw import *
from configparser import ConfigParser
import time


#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

alarminfo = config_object["ALARMINFO"]
counters = config_object["COUNTERS"]

frameThreshold = int( counters["frameThreshold"])
duration = float ( alarminfo["duration"] ) # seconds "alarm duration"
freq = float(  alarminfo["freq"]  ) # Hz

# latencyTimes = []

count = 0

# this methods fetches the frames from the camera and then finds the face and landmarks on the faces and checks weather the eyes are closed of the person
# or the person is yawming for a threshold amound of frames and generates a alarm.

def gen_frames(camera):  # generate frame by frame from camera

    global out, capture,rec_frame,count
    while True:
        
        success, frame = camera.read() 
        if success:    
            start_time = time.process_time()  #start the timer to check the latency
            frame = cv2.flip(frame,1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = detector(gray)     #detect Faces in a frame

            for face in faces:

                landmarks = predictor(gray, face)   #detect landmarks in each face found one by one 
                
                if (checkDrowsiness(landmarks)):
                    count = count+1
                else:
                    count = 0
                
                if count>frameThreshold:     # comparing the current count of the drowsiness with the frame threshold 
                    freq = freq- ( float(  alarminfo["freqChange"]  )) 
                    duration=duration+ (float(  alarminfo["durationChange"]  )) 
                    frame=put_red_rectangle(frame,face)
                    frame=put_text(frame,face)
                    
                    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                else:
                    freq=float(  alarminfo["freq"]  )
                    duration = float ( alarminfo["duration"] )
                    frame=put_rectangle(frame,face)
            
            end_time=time.process_time() #end the timer to check the latency
            
            fps= camera.get(cv2.CAP_PROP_FPS)  
            frame=put_fps(frame,fps)
            frame=put_latency(frame,end_time-start_time)
            try:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass
