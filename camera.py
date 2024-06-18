import numpy as np
import cv2

cap = cv2.VideoCapture(0)               #gets access to the webcam

# cap = cv2.VideoCapture('video_name' )      #if u want to run an existing video file

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):          #takes the ordinal value to end the video/cam
        break

cap.release()
cv2.destroyAllWindows()