import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score
from sklearn.multioutput import MultiOutputRegressor
import matplotlib.pyplot as plt
from math import sqrt
import pickle
import os


# load the model from disk
RF_multi = pickle.load(open('model.sav', 'rb'))


import cv2
from gaze_tracking import GazeTracking
from pynput.mouse import Button,Controller


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
mouse = Controller()
set_data =0
data = []


fields = ['LeftX', 'RightX', 'LeftY', 'RightY','LeftW','LeftH','RighttW','RightH']

import time

# timeout variable can be omitted, if you use specific value in the while condition
timeout = 3*60   # [seconds]

timeout_start = time.time()


while time.time() < timeout_start + timeout:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    
    frame = cv2.flip(frame, 1)
    
    global a,b
    
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print('go')
        set_data=1
 

    l= str(left_pupil) 
    r= str(right_pupil)
    t= "None"
    ls=gaze.get_left_eyesize()
    rs=gaze.get_right_eyesize()

    if set_data== 1 and t != l and t!= r and str(ls) != t and str(rs) != t:
        cv2.putText(frame,'collecting data.....', (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        data=[left_pupil[0],left_pupil[1],right_pupil[0],right_pupil[1],ls[0],ls[1],rs[0],rs[1]]
        data = np.array(data)
        data = np.reshape(data, (1,8))
        dataDF = pd.DataFrame(data)
        dataDF.columns = fields
        result = RF_multi.predict(dataDF)[0]
        mouse.position=(result[0],result[1])
        #print(result)
        


        
    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) == 27:
        break

print(data)