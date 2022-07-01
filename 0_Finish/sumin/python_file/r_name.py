import builtins
from tkinter import *
import os
import tkinter
from tkinter import filedialog
from typing import Sized


win = tkinter.Tk()
win.title("파일명변경")
win.geometry("200x200")



def renew():
    file_path = filedialog.askdirectory(parent=win, initialdir="/", title = "폴더를 선택해주세요")
    file_name = os.listdir(file_path)
    n = len(file_name)
    for i in range(0,n):
        t_name = file_name[i]
        t2_name = t_name[4:20]
        n_name = t2_name[:-2]
        sort = t2_name[-3:]
        if sort == "M_1":
            os.rename(file_path +"/"+ file_name[i], file_path +"/수입신고서-" + n_name + ".pdf")
        elif sort == "M_2":
            os.rename(file_path +"/"+ file_name[i], file_path + "/수입신고필증-" + n_name + ".pdf")
        elif sort == "X_0":
            os.rename(file_path +"/"+ file_name[i], file_path + "/수출신고필증-" + n_name + ".pdf")
        elif sort == "X_1":
            os.rename(file_path +"/"+ file_name[i], file_path + "/수출신고서-" + n_name + ".pdf")
        else: 
            pass

def acct():
    file_path = filedialog.askdirectory(parent=win, initialdir="/", title = "폴더를 선택해주세요")
    file_name = os.listdir(file_path)
    n = len(file_name)
    for i in range(0,n):
        t_name = file_name[i]
        n_name = t_name[7:]
        # print(n_name)
        # head = t_name[:6]
        # print(file_path +"/"+ file_name[i])
        # print(file_path +"/"+n_name)
        os.rename(file_path +"/"+ file_name[i], file_path +"/"+n_name)
        


btn = Button(win, text="폴더 선택", command=renew)
btn.pack()
btn2 = Button(win, text="관리용", command=acct)
btn2.pack()

win.mainloop()