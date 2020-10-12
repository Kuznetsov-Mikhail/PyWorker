import time
import zmq
import base64
import cv2
import numpy as np

def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    print('results_receiver.bind done')
    collecter_data = {}
    while(True):
        result = results_receiver.recv_json()
        print(result['num'])
result_collector()

