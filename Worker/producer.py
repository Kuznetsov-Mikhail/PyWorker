import time
import zmq
import cv2
import base64
import copy
print('I am producer')
context = zmq.Context()
producer_sender = context.socket(zmq.PUSH)
producer_sender.bind("tcp://*:5555")
print('bind done\n')
cap = cv2.VideoCapture(0)
num = 0
while(True):
    try:
        _, frame = cap.read()
        frame = cv2.resize(frame, (320, 240))  # resize the frame
        cv2.imshow('I am producer', frame)
        _, frame = cv2.imencode('.jpg', frame)
        frame = base64.b64encode(frame).decode("utf-8")
        ndata = {'index':num, 'frame':frame}
        producer_sender.send_json(ndata)
        print('frame '+str(ndata['index'])+ ' sended')
        num+=1 
        time.sleep(0.5)
        cv2.waitKey(1)
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break