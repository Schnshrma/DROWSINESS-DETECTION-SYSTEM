from math import hypot# for the calculation of hypotenuse etc


def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


def compute_blinking_ratio(eye_points, facial_landmarks):#calculation of blinking ratio  
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y) 
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    
    
    ratio = hor_line_lenght / ver_line_lenght#ratio of both
    return ratio
#same for mouth

def compute_mouth_ratio(lips_points, facial_landmarks):
    left_point = (facial_landmarks.part(lips_points[0]).x, facial_landmarks.part(lips_points[0]).y)#
    right_point = (facial_landmarks.part(lips_points[2]).x, facial_landmarks.part(lips_points[2]).y)
    center_top = (facial_landmarks.part(lips_points[1]).x, facial_landmarks.part(lips_points[1]).y)
    center_bottom = (facial_landmarks.part(lips_points[3]).x, facial_landmarks.part(lips_points[3]).y)

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    if hor_line_lenght == 0:
        return ver_line_lenght
    ratio = ver_line_lenght / hor_line_lenght
    return ratio

def checkDrowsiness(landmarks):
        left_eye_ratio = compute_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = compute_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        # cv2.putText(frame, str(blinking_ratio), (0, 13), font, 0.5, (100, 100, 100))
        print("-----------------------------------FRAME START---------------------------------------")
        print("Left_eye_ratio = ",str(left_eye_ratio))
        print("Right_eye_ratio = ",str(right_eye_ratio))
        print("Blinking_ratio = "+str(blinking_ratio))
        print()
        

        inner_lip_ratio = compute_mouth_ratio([60,62,64,66], landmarks)#
        outter_lip_ratio = compute_mouth_ratio([48,51,54,57], landmarks)
        mouth_opening_ratio = (inner_lip_ratio + outter_lip_ratio) / 2
        # cv2.putText(frame, str(mouth_opening_ratio), (448, 13), font, 0.5, (100, 100, 100))
        print("Inner_lip_ratio = "+str(inner_lip_ratio))
        print("Outter_lip_ratio = "+str(outter_lip_ratio))
        print("Mouth_opening_ratio = "+str(mouth_opening_ratio))
        print()
        print()

        if ((mouth_opening_ratio > 0.38 and blinking_ratio > 4 ) or blinking_ratio > 4.5):
            print("**************DROWSY %************** 100")
            print()
            print("----------------------FRAME END----------------------------")
            return True
        else :
        
            '''here we are calculateing how much drowsy is the driver in  %'''
            
            
            mouth_per=(mouth_opening_ratio/0.38)*100
            blink_per=(blinking_ratio/4)*100
            print("Mouth per = ",mouth_per)
            print("blink per = ",blink_per)
            avg_mouth_blink_per=(mouth_per+blink_per)/2
            avg_blink_ratio=(blinking_ratio/4.5)*100
           
            drowsy_per=max(avg_mouth_blink_per,avg_blink_ratio)
            
            if((mouth_opening_ratio > 0.38)):
            	drowsy_per=avg_blink_ratio
            
            print("*************DROWSY %**************",str(drowsy_per))
            print()
            print("----------------------FRAME END----------------------------")
            return False
