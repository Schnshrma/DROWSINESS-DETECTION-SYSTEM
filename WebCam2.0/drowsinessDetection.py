from scipy.spatial import distance as dist 
import pickle
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

ratioInfo = config_object["RATIOTHRESHOLDS"]
blinkingRatioThreshold = float( ratioInfo["blinkingRatioThreshold"] ) 
mouthRatioThreshold = float ( ratioInfo["mouthRatioThreshold"] ) 

blinkingRatios = []
mouthRatios =[]

# This function computes distancee between the left and right landmark of the eyes and the distance between 
# the top and bottom points of the eyes and returns the ratio of the distace of the vertical and horizontal poitns. 
def compute_blinking_ratio(eye_points, facial_landmarks):#calculation of blinking ratio  
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y) 
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    top_left = (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y)
    bottom_left = (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)
    top_right = (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y)
    bottom_right = (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y)

    p2_p6 = dist.euclidean(top_left, bottom_left)
    p3_p5 = dist.euclidean(top_right, bottom_right)
	# Horizontal eye landmarks 
    p1_p4 = dist.euclidean(left_point, right_point)

    EAR = (p2_p6 + p3_p5) / (2.0 * p1_p4)
    return EAR

#  This function computes the distance between the horizontal and vertical landmark points on the lips 
#  and returns the ratio between the vertical and horizontal landmark points
def compute_mouth_ratio(lips_points, facial_landmarks):
    left_point = (facial_landmarks.part(lips_points[0]).x, facial_landmarks.part(lips_points[0]).y)#
    right_point = (facial_landmarks.part(lips_points[2]).x, facial_landmarks.part(lips_points[2]).y)
    center_top = (facial_landmarks.part(lips_points[1]).x, facial_landmarks.part(lips_points[1]).y)
    center_bottom = (facial_landmarks.part(lips_points[3]).x, facial_landmarks.part(lips_points[3]).y)

    hor_line_length = dist.euclidean(left_point, right_point)
    ver_line_length = dist.euclidean(center_top, center_bottom)

    if hor_line_length == 0:
        return ver_line_length
    ratio = ver_line_length / hor_line_length
    return ratio

#  This function computes the eye ratio and lip ratio from the face landmark points and then compared these ratio
#  values with the threshold values and return true and false based on the threshold value.
def checkDrowsiness(landmarks):
        left_eye_ratio = compute_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = compute_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        inner_lip_ratio = compute_mouth_ratio([60,62,64,66], landmarks)

        # blinkingRatios.append(blinking_ratio)
        # mouthRatios.append(inner_lip_ratio)
        
        if(blinking_ratio < blinkingRatioThreshold or ( inner_lip_ratio > mouthRatioThreshold ) ):
            return True
        else: 
            return False

# saves the the eye ratio values in file
def saveEyeBlinkingRatio():
    with open("data/eyeBlinkingData3", "wb") as fp:   
        pickle.dump(blinkingRatios, fp)

# saves the mouthe ratio value in file
def saveMouthRatio():
     with open("data/mouthData2", "wb") as fp:  
        pickle.dump(mouthRatios, fp)
