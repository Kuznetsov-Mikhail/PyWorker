import cv2
from Worker_module import worker
cap = cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    frame = cv2.resize(frame, (320, 240))  # resize the frame
    cv2.imshow('not mult', frame)
    frame = worker.cartoon_from_frame(frame)    
    cv2.imshow('mult', frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()