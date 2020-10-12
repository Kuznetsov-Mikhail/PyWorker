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
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    print('consumer_receiver.connect done')
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")
    print('consumer_sender.connect done')
    
    while True:
        work = consumer_receiver.recv_json()
        frame = worker.cartoon_from_frame(frame)
        result = { 'frame' : frame, 'num' : work['num']}
        consumer_sender.send_json(result)
consumer()
