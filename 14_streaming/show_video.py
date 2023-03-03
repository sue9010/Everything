import cv2
import numpy as np


def show_video(video1, video2):
    cap1 = cv2.VideoCapture(video1)
    cap2 = cv2.VideoCapture(video2)

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break
        cv2.imshow("Combined Video", np.hstack((frame1, frame2)))
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
