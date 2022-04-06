import cv2

def put_red_rectangle(face,frame):
    x,y = face.left(), face.top()
    x1,y1 = face.right(), face.bottom()
    cv2.rectangle(frame, (x,y), (x1,y1), (0, 0, 255), 2)
    return frame


def put_text(face,frame):
    font = cv2.FONT_HERSHEY_TRIPLEX   # for font of image 
    x,y = face.left(), face.top()
    x1,y1 = face.right(), face.bottom()    
    cv2.putText(frame, "Drowsing", (x, y-5), font, 0.5, (0, 0, 255))
    return frame


def put_rectangle(face,frame):
    x,y = face.left(), face.top()
    x1,y1 = face.right(), face.bottom()
    cv2.rectangle(frame, (x,y), (x1,y1), (0, 255, 0), 2)
    return frame

