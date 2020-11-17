import time
import zmq
import random
import base64
import cv2
import numpy as np
import copy
from Worker_module import worker
consumer_id = random.randrange(1,10005)
print("I am worker #%s"%(consumer_id))
context = zmq.Context()
# recieve work
consumer_receiver = context.socket(zmq.PULL)
consumer_receiver.connect("tcp://192.168.1.130:5555")
# send work
consumer_sender = context.socket(zmq.PUSH)
consumer_sender.connect('tcp://192.168.1.61:5556')
print('connect done\n')  
while True:
    try:
        data = consumer_receiver.recv_json()
        print('frame '+str(data['index'])+ ' recved')
        frame = base64.b64decode(data['frame'])
        frame = np.fromstring(frame, dtype=np.uint8)
        frame = cv2.imdecode(frame, 1)
        nframe = worker.cartoon_from_frame(frame)
        _, nframe = cv2.imencode('.jpg', nframe)
        nframe = base64.b64encode(nframe).decode("utf-8")
        ndata = {'index':data['index'], 'frame':nframe}
        consumer_sender.send_json(ndata)
        print('frame '+str(ndata['index'])+ ' sended')
        cv2.waitKey(1)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break