import tkinter as tk
from show_video import show_video

root = tk.Tk()
root.title("Tkinter + OpenCV Example")

tk.Label(root, text="RTSP Address 1:").grid(row=0, column=0, sticky="W")
entry1 = tk.Entry(root, width=40)
entry1.insert(0, "rtsp://192.168.0.10/PSIA/Streaming/channels/0")
entry1.grid(row=0, column=1)

tk.Label(root, text="RTSP Address 2:").grid(row=1, column=0, sticky="W")
entry2 = tk.Entry(root, width=40)
entry2.insert(0, "rtsp://192.168.0.16/PSIA/Streaming/channels/0")
entry2.grid(row=1, column=1)

tk.Button(root, text="Show Video", command=lambda: show_video(entry1.get(), entry2.get())).grid(
    row=2, column=0, columnspan=2, pady=10)
root. mainloop()
