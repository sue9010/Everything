import cv2 
import numpy as np
import requests
import time
# 샘플 영상 

url = 'rtsp://admin:cg600ip100m@192.168.0.34/PSIA/Streaming/channels/0 : Stream 0' 
cap = cv2.VideoCapture(url) 
# fps = 20.0
# width = int(cap.get(3))
# height = int(cap.get(4))
# fcc = cv2.VideoWriter_fourcc('D','I','V','X')

# out= cv2.VideoWriter(url, fcc, fps, (width, height))

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

while True : 
    ret, frame = cap.read()
    # if not ret:
    #     break
    __draw_label(frame, get_max_temp(),(200,200),(255,255,255))

# 윈도우 창 출력용 
    cv2.imshow("video", frame)
    cv2.waitKey(1)
 
#     out.write(frame)

#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()


