import cv2
import numpy as np
import requests
import datetime
import os

url = 'rtsp://admin:cg600ip100m@192.168.0.200/PSIA/Streaming/channels/0 : Stream 0' 
dt_now = datetime.datetime.now()

def get_max_temp():
    text = "http://admin:cg600ip100m@192.168.0.34/cgi-bin/httpapi/thermal.cgi?svc=tempAdvInfo&action=gets"
    response = requests.get(text)
    txt = response.text
    target = "max_temp_value="
    ntarget = "avr_temp_value"
    sn=txt.rfind(target)
    ln=txt.rfind(ntarget)
    show_text = "MAX:" + txt[sn+15:ln-2]
    return show_text

def __draw_label(img, text, pos, bg_color):
   font_face = cv2.FONT_HERSHEY_SIMPLEX
   scale = 1
   color = (0, 0, 0)
   thickness = cv2.FILLED
   margin = 2
   txt_size = cv2.getTextSize(text, font_face, scale, thickness)

   end_x = pos[0] + txt_size[0][0] + margin
   end_y = pos[1] - txt_size[0][1] - margin

   cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
   cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)


def writeVideo():
    video_capture = cv2.VideoCapture(url)
    video_capture.set(3,640)
    video_capture.set(4,480)
    fps = 20
    streaming_window_width = int(video_capture.get(3))
    streaming_window_height = int(video_capture.get(4))

    fileName = str(dt_now.strftime('%Y-%m-%d %H%M%S'))

    path = f'E:/PythonPractice/video/{fileName}.avi'

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    out = cv2.VideoWriter(path, fourcc, fps, (streaming_window_width, streaming_window_height))

    while True:
        ret, frame = video_capture.read()
        __draw_label(frame, get_max_temp(),(200,200),(255,255,255))
        # 촬영되는 영상보여준다. 프로그램 상태바 이름은 'streaming video' 로 뜬다.
        cv2.imshow('streaming video', frame)
        
        # 영상을 저장한다.
        out.write(frame)
        
        # 1ms뒤에 뒤에 코드 실행해준다.
        k = cv2.waitKey(1) & 0xff
        #키보드 esc 누르면 종료된다.
        if k == 27:
            break
        
    video_capture.release()  # cap 객체 해제
    out.release()  # out 객체 해제
    cv2.destroyAllWindows()

if __name__ == "__main__":
    writeVideo()
