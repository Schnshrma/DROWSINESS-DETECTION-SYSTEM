from scipy.spatial import distance as dist 

blinkingRatios = []
mouthRatios =[]
def getBlinkingRatios():
    return blinkingRatios

def getMouthRatios():
    return mouthRatios

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

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
    # print(EAR)
    return EAR


def compute_mouth_ratio(lips_points, facial_landmarks):
    left_point = (facial_landmarks.part(lips_points[0]).x, facial_landmarks.part(lips_points[0]).y)#
    right_point = (facial_landmarks.part(lips_points[2]).x, facial_landmarks.part(lips_points[2]).y)
    center_top = (facial_landmarks.part(lips_points[1]).x, facial_landmarks.part(lips_points[1]).y)
    center_bottom = (facial_landmarks.part(lips_points[3]).x, facial_landmarks.part(lips_points[3]).y)

    hor_line_lenght = dist.euclidean(left_point, right_point)
    ver_line_lenght = dist.euclidean(center_top, center_bottom)

    if hor_line_lenght == 0:
        return ver_line_lenght
    ratio = ver_line_lenght / hor_line_lenght
    return ratio

def checkDrowsiness(landmarks):
        left_eye_ratio = compute_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = compute_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        inner_lip_ratio = compute_mouth_ratio([60,62,64,66], landmarks)

        # blinkingRatios.append(blinking_ratio)
        # mouthRatios.append(inner_lip_ratio)
        # print(str(inner_lip_ratio) +" ----  "+ str(blinking_ratio))
        # return False
        if(blinking_ratio < 0.20 or inner_lip_ratio > 0.38 ):
            return True
        else: 
            return False
