import time
import zmq
import cv2


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    ########################################
    #cap = cv2.VideoCapture(0)
    #ret, frame = cap.read()
    # Start your result manager and workers before you start your producers
    for num in range(20000):
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)

producer()
