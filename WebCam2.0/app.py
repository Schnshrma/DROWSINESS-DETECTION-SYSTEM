from flask import Flask, render_template
from flask_socketio import SocketIO,emit
import cv2
import imutils
from PIL import Image
import io
import numpy as np
import base64
from io import StringIO 
from flask_cors import CORS, cross_origin
from launchDrowsinessDetection import *

app = Flask(__name__)
cors = CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")



@app.route('/')
@cross_origin()
def index():
    	# rendering webpage
	return render_template('index.html')

@socketio.on('image')
def image(data_image):

    sbuf = StringIO()    
    sbuf.write(data_image)

    arrayData = data_image.split(',')
    data_image = arrayData[0]
    timeStamp = arrayData[1]
    
    # decode and convert into image   
    b = io.BytesIO(base64.b64decode(data_image))    
    pimg = Image.open(b)    
    
    ## converting RGB to BGR, as opencv standards    
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)    
    
    # Process the image frame    
    frame = imutils.resize(frame, width=700)    
    frame = cv2.flip(frame, 1)  
    
    frame,status = checkFrame(frame)

    imgencode = cv2.imencode('.jpg', frame)[1]    

    # base64 encode    
    stringData = base64.b64encode(imgencode).decode('utf-8')    
    b64_src = 'data:image/png;base64,'    
    stringData = b64_src + stringData +"|"+timeStamp
    
    # emit the frame back    
    emit('response_back', stringData)
    if(status == True):
        emit('raise_alarm',status)

socketio.run(app, host='127.0.0.1')

