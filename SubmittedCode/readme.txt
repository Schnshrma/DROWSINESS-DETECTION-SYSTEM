Drowsiness Detection Application

1.Install the packages given in requirements.txt - pip install requirements.txt
2.Download and copy the shape_predictor_68_face_landmarks.dat file and paste the file in the project directory.
3. To start the application run - python3 startWebApp.py
   Terminal will show the url at which the application is running.


launchDrowsinessDetection.py - File contains gen_frames method which first checks for faces in each frame then finds facial landmarks on the faces detected and then check the ratio of eyes and mouth and decides weather the user is drowsiee or not based on the threshold set of the number of frames.
