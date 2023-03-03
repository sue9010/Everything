import tkinter as tk
import numpy as np
import cv2


def show_video():
    cap1 = cv2.VideoCapture(entry1.get())
    cap2 = cv2.VideoCapture(entry2.get())

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break
        combined = np.concatenate((frame1, frame2), axis=1)
        cv2.imshow("Combined Video", combined)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


root = tk.Tk()
root.title("Tkinter + OpenCV Example")

label1 = tk.Label(root, text="RTSP Address 1:")
label1.grid(row=0, column=0, sticky="W")

entry1 = tk.Entry(root, width=40)
entry1.insert(0, "rtsp://192.168.0.10/PSIA/Streaming/channels/0")
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="RTSP Address 2:")
label2.grid(row=1, column=0, sticky="W")

entry2 = tk.Entry(root, width=40)
entry2.insert(0, "rtsp://192.168.0.16/PSIA/Streaming/channels/0")
entry2.grid(row=1, column=1)

button = tk.Button(root, text="Show Video", command=show_video)
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
