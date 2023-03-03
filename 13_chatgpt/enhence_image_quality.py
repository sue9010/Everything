import cv2

# Open the video file
cap = cv2.VideoCapture(r"E:\PythonPractice\Everything\13_chatgpt\video.mp4")

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('enhanced_video.avi', fourcc, 20.0,
                      (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization to the grayscale frame
    gray_equalized = cv2.equalizeHist(gray)
    # Convert the equalized grayscale frame back to color
    frame_equalized = cv2.cvtColor(gray_equalized, cv2.COLOR_GRAY2BGR)
    # Display the equalized frame
    cv2.imshow("Frame", frame_equalized)
    out.write(frame_equalized)
    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()
# Close all the windows
cv2.destroyAllWindows()
