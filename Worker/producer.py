import time
import zmq
import cv2
import base64

cap = cv2.VideoCapture(0)
def producer():
    context = zmq.Context()
    producer_sender = context.socket(zmq.PUSH)
    producer_sender.bind("tcp://127.0.0.1:5557")
    print('producer_sender.bind done')
    ########################################
    num = 0
    while(True):
        try:
            _, frame = cap.read()
            frame = cv2.resize(frame, (640, 480))
            work_message = { 'num' : num, 'frame':(frame) }
            producer_sender.send_json(work_message)
            num+=1 
        except KeyboardInterrupt:
            cap.release()
            cv2.destroyAllWindows()
            print("\n\nBye bye\n")
            break
producer()