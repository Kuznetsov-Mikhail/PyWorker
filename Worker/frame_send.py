import cv2
import zmq
import base64

context = zmq.Context()
footage_socket = context.socket(zmq.PUSH)
footage_socket.connect('tcp://localhost:5555')

camera = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        (_, frame) = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        _, frame = cv2.imencode('.jpg', frame)
        frame = base64.b64encode(frame).decode("utf-8")
        data = {'index':0, 'frame':frame}
        footage_socket.send_json(data)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break