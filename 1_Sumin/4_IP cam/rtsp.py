from webbrowser import get
import cv2
import tkinter
from tkinter import Tk


window = tkinter.Tk()

window.title("Streaming")
window.geometry("640x480")
window.resizeable(False, False)

label = tkinter.Label(window, get_stream(url))
label.pack()

window.mainloop()

url = 'rtsp://admin:cg600ip100m@169.254.0.100/PSIA/Streaming/channels/0 : Stream 0'


def get_stream(url):
    cap = cv2.VideoCapture(url)
    while True:
        ret, frame = cap.read()
        cv2.imshow("video", frame)
        cv2.waitKey(1)
