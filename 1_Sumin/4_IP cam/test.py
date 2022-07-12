import tkinter as tk  # Tkinter
from PIL import ImageTk, Image  # Pillow
import cv2 as cv  # OpenCV
import os
import cv2


win = tk.Tk()  # 인스턴스 생성

win.title("IP camera")  # 제목 표시줄 추가
win.geometry("640x480")  # 지오메트리: 너비x높이+x좌표+y좌표
win.resizable(False, False)  # x축, y축 크기 조정 비활성화

lbl = tk.Label(win, text="Tkinter와 OpenCV를 이용한 GUI 프로그래밍")
lbl.grid(row=0, column=0)  # 라벨 행, 열 배치
frm = tk.Frame(win, bg="white", width=720, height=480)  # 프레임 너비, 높이 설정
frm.grid(row=1, column=0)  # 격자 행, 열 배치
lbl1 = tk.Label(frm)
lbl1.grid()


def video_play():
    url = 'rtsp://admin:cg600ip100m@169.254.0.100/PSIA/Streaming/channels/0 : Stream 0'
    cap = cv2.VideoCapture(url)

# while True:
    ret, frame = cap.read()  # 프레임이 올바르게 읽히면 ret은 True
    if not ret:
        cap.release()  # 작업 완료 후 해제
        return

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img = Image.fromarray(frame)  # Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=img)  # ImageTk 객체로 변환

    # OpenCV 동영상
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(5, video_play)


video_play()

win.mainloop()  # GUI 시작
