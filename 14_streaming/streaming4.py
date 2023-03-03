import tkinter as tk
import cv2
import numpy as np


def show_video():
    video1 = entry1.get()
    video2 = entry2.get()
    video3 = entry3.get()
    video4 = entry4.get()
    cap1 = cv2.VideoCapture(video1)
    cap2 = cv2.VideoCapture(video2)
    cap3 = cv2.VideoCapture(video3)
    cap4 = cv2.VideoCapture(video4)

    while True:
        # Read the frames from the video streams
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        ret3, frame3 = cap3.read()
        ret4, frame4 = cap4.read()

        # Check if frames are read successfully
        if not ret1 or not ret2 or not ret3 or not ret4:
            break

        # Stack the frames vertically
        combined1 = np.vstack((frame1, frame2))
        combined2 = np.vstack((frame3, frame4))
        combined = np.hstack((combined1, combined2))

        # Display the combined frames
        cv2.imshow("Combined Video", combined)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video streams
    cap1.release()
    cap2.release()
    cap3.release()
    cap4.release()

    # Destroy all windows
    cv2.destroyAllWindows()


# Create the main window
root = tk.Tk()
root.title("Tkinter + OpenCV Example")

# Create labels and entry widgets
label1 = tk.Label(root, text="RTSP Address 1:")
label1.grid(row=0, column=0, sticky="W")

entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="RTSP Address 2:")
label2.grid(row=0, column=2, sticky="W")

entry2 = tk.Entry(root, width=20)
entry2.grid(row=0, column=3)

label3 = tk.Label(root, text="RTSP Address 3:")
label3.grid(row=1, column=0, sticky="W")

entry3 = tk.Entry(root, width=20)
entry3.grid(row=1, column=1)

label4 = tk.Label(root, text="RTSP Address 4:")
label4.grid(row=1, column=2, sticky="W")

entry4 = tk.Entry(root, width=20)
entry4.grid(row=1, column=3)

# Create a button
button = tk.Button(root, text="Show Video", command=show_video)
button.grid(row=2, column=0, columnspan=4, pady=10, sticky="W" + "E")

# Start the main event loop
root.mainloop()
