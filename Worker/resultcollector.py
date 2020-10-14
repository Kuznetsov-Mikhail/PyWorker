import time
import zmq
import base64
import cv2
import numpy as np
import copy
from threading import Thread
print('I am resultcollector')
context = zmq.Context()
results_receiver = context.socket(zmq.PULL)
results_receiver.bind("tcp://*:5556")
print('bind done\n')
collector_data = {}
num = 0
while True:
    data = results_receiver.recv_json()
    print('frame '+str(data['index'])+ ' recved')
    frame = base64.b64decode(data['frame'])
    frame = np.fromstring(frame, dtype=np.uint8)
    frame = cv2.imdecode(frame, 1)
    ndata = {'frame':frame, 'index':data['index']}
    collector_data[int(data['index'])]=frame
    try:
        pic = collector_data.pop(num)
        cv2.imshow('I am collector', pic)
        num+=1
        cv2.waitKey(1)
    except KeyError:
        continue
