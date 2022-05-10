import cv2

def put_red_rectangle(frame,face):
    x,y = face.left(), face.top()
    x1,y1 = face.right(), face.bottom()
    cv2.rectangle(frame, (x,y), (x1,y1), (0, 0, 255), 2)
    return frame


def put_text(frame,face):
    font = cv2.FONT_HERSHEY_TRIPLEX   # for font of image 
    x,y = face.left(), face.top()
    x1,y1 = face.right(), face.bottom()    
    cv2.putText(frame, "Drowsing", (x, y-5), font, 0.5, (0, 0, 255))
    return frame


def put_rectangle(frame,face):
    x,y = face.left(), face.top()
    x1,y1 = face.right(), face.bottom()
    cv2.rectangle(frame, (x,y), (x1,y1), (0, 255, 0), 2)
    return frame

def put_latency(frame,text):
    latency = float(text)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Latency : "+str("%.4f" % round(latency,4)), (20, 50), font, 0.5, (0, 255, 0), 1)
    return frame

def put_fps(frame,text):
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, "fps: "+str(text),(20, 80), font, 0.5, (0, 255, 0), 1)
	return frame
