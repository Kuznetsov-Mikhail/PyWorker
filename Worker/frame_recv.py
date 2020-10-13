import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.PULL)
footage_socket.bind('tcp://*:5555')


while True:
    try:
        data = footage_socket.recv_json()
        frame = base64.b64decode(data['frame'])
        frame = np.fromstring(frame, dtype=np.uint8)
        frame = cv2.imdecode(frame, 1)
        cv2.imshow("image", frame)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break