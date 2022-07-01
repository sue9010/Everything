from tkinter import *
import tkinter
import pyautogui

win = tkinter.Tk()
win.geometry("230x75")
win.title("Unipass")
win.resizable(0,0)

label1= Label(win, text="ID:", width=10)
label1.grid(row=0,column=0)
entry1= Entry(win, textvariable="inputId", width=20)
entry1.grid(row=0,column=1)
label2= Label(win, text="PW:", width=10)
label2.grid(row=1,column=0)
entry2= Entry(win, textvariable="inputPw", width=20, show="*")
entry2.grid(row=1,column=1)





def COX():
    entry1= Entry(win, text= "coxcamera", width=20)
    entry1.grid(row=0,column=1)
    entry2= Entry(win, textvariable="inputPw", width=20)
    entry2.grid(row=1,column=1)


button0 =Button(win, text="COX", width=8, command=COX)
button0.grid(row=2, column=0)
button1 = Button(win, text="Log in", width=20)
button1.grid(row=2, column=1)


win.mainloop()