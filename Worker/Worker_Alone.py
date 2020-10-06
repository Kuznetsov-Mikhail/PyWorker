import cv2
from Worker_module import worker
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = worker.cartoon_from_frame(frame)    
    cv2.imshow('frame', frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()