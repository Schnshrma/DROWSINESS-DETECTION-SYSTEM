from flask import Flask, render_template
from flask_socketio import SocketIO , emit
import cv2
import imutils
from PIL import Image
import io
import numpy as np
import base64
from io import StringIO 
import zlib
from launchDrowsinessDetection import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my_event')
def handle_my_custom_event(json):
    emit('my_response', json)

@socketio.on('image')
def image(data_image):
    sbuf = StringIO()    
    sbuf.write(data_image)
    
    arrayData = data_image.split(',')
    
    
    timeStamp = arrayData[len(arrayData)-1]
    # print(timeStamp)
    # desired_array = [int(numeric_string) for numeric_string in arrayData[0:len(arrayData)-1]]
    # data_image = zlib.decompress(bytes(desired_array))
    data_image = arrayData[0]
    # decode and convert into image   
    b = io.BytesIO(base64.b64decode(data_image))    
    pimg = Image.open(b)    
    
    ## converting RGB to BGR, as opencv standards    
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)    
    
    # Process the image frame    
    # frame = imutils.resize(frame, width=700)    
    frame = cv2.flip(frame, 1)  

    frame,status = checkFrame(frame)

    imgencode = cv2.imencode('.jpg', frame)[1]    

    # base64 encode    
    stringData = base64.b64encode(imgencode).decode('utf-8')   
    # stringData = zlib.compress(stringData.encode()) 
    # b64_src = 'data:image/png;base64,' 
    # int_values = [x for x in stringData]

    # int_values =  str(int_values) +"timestamp"+timeStamp

    int_values =  stringData +"timestamp"+timeStamp
    
    # emit the frame back    
    emit('response_back', int_values)
    if(status == True):
        emit('raise_alarm',status)


if __name__ == '__main__':
    socketio.run(app)