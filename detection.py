import dlib#For face recognition
'''
def dectector():
    detector = dlib.get_frontal_face_detector()#face detected
    return detector

def predictor():
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")#for getting all 68 quardinates of face
    return predictor
'''
detector = dlib.get_frontal_face_detector()#face detected

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")#for getting all 68 quardinates of face
