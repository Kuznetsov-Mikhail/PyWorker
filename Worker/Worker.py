import numpy as np
import cv2
import zmq
import time
import sys

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            for k in range(3):
                buf = int(frame[i,j,k]/64)
                frame[i,j,k] = buf*64 +32
    cv2.imshow('frame', frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()