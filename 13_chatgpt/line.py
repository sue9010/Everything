import cv2

# Load the human classifier
human_cascade = cv2.CascadeClassifier(
    r"D:\Software\python\Lib\site-packages\cv2\data\haarcascade_fullbody.xml")

# Open the video file
cap = cv2.VideoCapture(r"E:\PythonPractice\Everything\13_chatgpt\video.mp4")

# Get the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect humans in the frame
    humans = human_cascade.detectMultiScale(gray, 1.1, 5)
    # Draw a line of 10 pixels around each human
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
    # Display the frame
    cv2.imshow("Frame", frame)
    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
# Close all the windows
cv2.destroyAllWindows()
