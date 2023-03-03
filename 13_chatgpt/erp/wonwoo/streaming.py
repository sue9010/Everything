import cv2
import numpy as np

# Define the RTSP addresses
video_1 = "rtsp://192.168.0.10/PSIA/Streaming/channels/0"
video_2 = "rtsp://192.168.0.16/PSIA/Streaming/channels/0"

# Start capturing the video streams
cap1 = cv2.VideoCapture(video_1)
cap2 = cv2.VideoCapture(video_2)

while True:
    # Read the frames from the video streams
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Check if frames are read successfully
    if not ret1 or not ret2:
        break

    # Stack the frames horizontally
    combined = np.hstack((frame1, frame2))

    # Display the combined frames
    cv2.imshow("Combined Video", combined)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video streams
cap1.release()
cap2.release()

# Destroy all windows
cv2.destroyAllWindows()
