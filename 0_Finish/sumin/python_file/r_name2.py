from tkinter import *
import os
import tkinter
from tkinter import filedialog

win= tkinter.Tk()
win.geometry("260x60")
win.title("test")

def pretty():
    win.withdraw()
    file_path = filedialog.askdirectory(parent=win, initialdir="/", title = "폴더를 선택해주세요")
    file_name = os.listdir(file_path)
    n = len(file_name)
    for i in range(0,n):
        t_name = file_name[i]
        n_name = t_name[4:20]
        os.rename(file_path + "/" +t_name, file_path + "/" + n_name + ".pdf")
    print("완료")

def renew():
    win.withdraw()
    file_path = filedialog.askdirectory(parent=win, initialdir="/", title = "폴더를 선택해주세요")
    file_name = os.listdir(file_path)
    n = len(file_name)
    for i in range(0,n):
        r_name = file_name[i]
        f_name = r_name[:14]
        sort = r_name[-7:-4]
        if sort == "M_1":
            os.rename(file_path+ "/" + r_name, file_path+ "/수입신고서-" + f_name + ".pdf")
        elif sort == "M_2":
            os.rename(file_path+ "/"+ r_name, file_path + "수입신고필증-" + f_name + ".pdf")
        elif sort == "X_0":
            os.rename(file_path+ "/"+ r_name, file_path + "/수출신고필증-" + f_name + ".pdf")
        elif sort == "X_1":
            os.rename(file_path+ "/"+ r_name, file_path + "/수출신고서-" + f_name + ".pdf")
        else: 
            pass
    i = i + 1
    print("완료")

btn1 = Button(win, text= "pretty", width=10, command=pretty)
btn1.grid(row=0,column=2)
btn2 = Button(win, text= "renew", width=10, command=renew)
btn2.grid(row=1,column=2)


win.mainloop()