import time
import zmq
import random
import base64
import cv2
import numpy as np
from Worker_module import worker

def consumer():
    consumer_id = random.randrange(1,10005)
    print("I am worker #%s"%(consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.bind("tcp://127.0.0.1:5557")
    print('consumer_receiver.connect done')
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")
    print('consumer_sender.connect done')
    
    while True:
        data = consumer_receiver.recv_json()
        frame = base64.b64decode(data['frame'])
        frame = np.fromstring(frame, dtype=np.uint8)
        frame = cv2.imdecode(frame, 1)
        cv2.imshow(str("worker "+str(consumer_id)), frame)
        #frame = worker.cartoon_from_frame(frame)
        #_, frame = cv2.imencode('.jpg', frame)
        #frame = base64.b64encode(frame).decode("utf-8")
        #result = { 'frame' : frame, 'num' : data['index']}
        #consumer_sender.send_json(result)
consumer()
