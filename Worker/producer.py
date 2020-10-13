import time
import zmq
import cv2
import base64

cap = cv2.VideoCapture(0)
def producer():
    context = zmq.Context()
    producer_sender = context.socket(zmq.PUSH)
    producer_sender.connect("tcp://127.0.0.1:5557")
    print('producer_sender.bind done')
    ########################################
    num = 0
    while(True):
        try:
            _, frame = cap.read()
            frame = cv2.resize(frame, (640, 480))  # resize the frame
            _, frame = cv2.imencode('.jpg', frame)
            frame = base64.b64encode(frame).decode("utf-8")
            data = {'index':num, 'frame':frame}
            producer_sender.send_json(data)
            num+=1 
        except KeyboardInterrupt:
            cap.release()
            cv2.destroyAllWindows()
            print("\n\nBye bye\n")
            break
producer()