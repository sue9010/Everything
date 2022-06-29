import os
import tkinter
from tkinter import filedialog  
from tkinter import *

# tkinter로 창 실행
window = tkinter.Tk()

# 창 타이틀 설정
window.title("필증 파일명 변경")
# 창 크기 설정
window.geometry("300x100")
# 창 리사이즈 불가능 설정
window.resizable(False,False)

def rename():
    # 폴더 선택 창 열기
    window.dirName = filedialog.askdirectory()
    # 폴더 경로를 받아오기
    file_path = window.dirName
    # 폴더 안에 있는 파일명을 리스트 형태로 받아오기
    file_names = os.listdir(file_path)

    for name in file_names:
        # 폴더 경로 + 파일명 -> 기존 파일명
        old_name = file_path + "\\"+ name
        # 폴더 경로 + 슬라이싱 한 파일명 -> 새로운 파일명
        new_name = file_path + "\\"+ name[4:18]+".pdf"
        # 파일명 변경 명령문
        os.rename(old_name, new_name)

# 폴더 선택 버튼 생성
btn = tkinter.Button(window, text="경로 선택 및 파일명 변경",command=rename)
# 폴더 선택 버튼 위치 지정
btn.pack()

# 창 유지
window.mainloop()


