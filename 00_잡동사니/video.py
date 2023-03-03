import cv2
import time

# Open the RTSP streams
cap1 = cv2.VideoCapture('rtsp://192.168.0.51/PSIA/Streaming/channels/0')
cap2 = cv2.VideoCapture('rtsp://192.168.0.24/PSIA/Streaming/channels/0')

# Set the frame rate
frame_rate = 9
frame_interval = 1.0 / frame_rate

# Read and display frames from the streams in a single window
while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    ret2, frame2 = cap2.read()
    if not ret2:
        break

    # Combine the frames into a single image
    combined = cv2.hconcat([frame1, frame2])
    cv2.imshow('Video', combined)

    if cv2.waitKey(1) == 27:
        break

    # Sleep for the required interval
    time.sleep(frame_interval)

# Release the streams
cap1.release()
cap2.release()
