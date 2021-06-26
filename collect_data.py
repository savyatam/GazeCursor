import cv2
from gaze_tracking import GazeTracking
from pynput.mouse import Button,Controller
import csv



gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
mouse = Controller()
set_data =0
data = []


fields = ['CursorX','CursorY','LeftX', 'RightX', 'LeftY', 'RightY','LeftW','LeftH','RighttW','RightH']
# name of csv file 
filename = "data.csv"
    

import time

# timeout variable can be omitted, if you use specific value in the while condition
timeout = 5*60   # [seconds]

timeout_start = time.time()


while time.time() < timeout_start + timeout:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    
    frame = cv2.flip(frame, 1)
    
    global a,b
    
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    # get left eye and right eye positions
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print('go') # start collecting data  
        set_data=1
 

    l= str(left_pupil) 
    r= str(right_pupil)
    t= "None" 
    x= mouse.position[0] # cursor positions
    y= mouse.position[1]
    ls=gaze.get_left_eyesize() # left_eye size i.e dimesnions (width and height)
    rs=gaze.get_right_eyesize() # right_eye size i.e dimesnions (width and height)



    if set_data== 1 and t != l and t!= r and str(ls) != t and str(rs) != t:
        cv2.putText(frame,'collecting data.....', (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        data.append([x,y,left_pupil[0],left_pupil[1],right_pupil[0],right_pupil[1],ls[0],ls[1],rs[0],rs[1]])
        
    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) == 27:
        break

print(data)
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields)
    csvwriter.writerows(data) 

