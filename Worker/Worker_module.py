import cv2
class worker:
    def cartoon_from_frame(frame):
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                for k in range(3):
                    buf = int(frame[i,j,k]/64)
                    frame[i,j,k] = buf*64 +32
        return frame
