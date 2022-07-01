from tkinter import *
import tkinter
import pyautogui
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

win = tkinter.Tk()
win.title ("AF test recording")

af = pyautogui.locateAllOnScreen(resource_path("autofocus.png"))
record = pyautogui.locateOnScreen(resource_path("record.png"))
focus = pyautogui.locateOnScreen(resource_path("focus.png"))
record2 = pyautogui.locateOnScreen(resource_path("record2.png"))

def click_button():
    for i in pyautogui.locateAllOnScreen(resource_path("focus.png")):
        pyautogui.moveTo(i)
        pyautogui.move(1261-1202,857-856)

        # print(i)
        pyautogui.mouseDown()
        pyautogui.sleep(5)
        pyautogui.mouseUp() 

    for k in pyautogui.locateAllOnScreen(resource_path("record.png")):
        pyautogui.click(k,duration=0.15)

    for j in pyautogui.locateAllOnScreen(resource_path("autofocus.png")):
        pyautogui.click(j)


    pyautogui.sleep(5)


    for k in pyautogui.locateAllOnScreen(resource_path("record2.png")):
        pyautogui.click(k,duration=0.15)

def click_button2():
    for i in pyautogui.locateAllOnScreen(resource_path("focus.png")):
        pyautogui.moveTo(i)
        pyautogui.move(-60,0)

        # print(i)
        pyautogui.mouseDown()
        pyautogui.sleep(5)
        pyautogui.mouseUp() 

    for k in pyautogui.locateAllOnScreen(resource_path("record.png")):
        pyautogui.click(k,duration=0.15)

    for j in pyautogui.locateAllOnScreen(resource_path("autofocus.png")):
        pyautogui.click(j)


    pyautogui.sleep(5)


    for k in pyautogui.locateAllOnScreen(resource_path("record2.png")):
        pyautogui.click(k,duration=0.15)

def click_button3():
    for i in pyautogui.locateAllOnScreen(resource_path("focus.png")):
        pyautogui.moveTo(i)
        pyautogui.move(-60,0)

        # print(i)
        pyautogui.mouseDown()
        pyautogui.sleep(5)
        pyautogui.mouseUp() 

    for k in pyautogui.locateAllOnScreen(resource_path("record.png")):
        pyautogui.click(k,duration=0.15)

    for j in pyautogui.locateAllOnScreen(resource_path("autofocus.png")):
        pyautogui.click(j)


    pyautogui.sleep(5)


    for k in pyautogui.locateAllOnScreen(resource_path("record2.png")):
        pyautogui.click(k,duration=0.15)

def click_button4():
    for i in pyautogui.locateAllOnScreen(resource_path("focus.png")):
        pyautogui.moveTo(i)
        pyautogui.move(-60,0)

        # print(i)
        pyautogui.mouseDown()
        pyautogui.sleep(5)
        pyautogui.mouseUp() 

    for k in pyautogui.locateAllOnScreen(resource_path("record.png")):
        pyautogui.click(k,duration=0.15)

    for j in pyautogui.locateAllOnScreen(resource_path("autofocus.png")):
        pyautogui.click(j)


    pyautogui.sleep(5)


    for k in pyautogui.locateAllOnScreen(resource_path("record2.png")):
        pyautogui.click(k,duration=0.15)

button1 = Button(win, text="+5", font=("맑은 고딕", 25), command=click_button)
button1.place(x=250,y=100,width=100,height=50)

button2 = Button(win, text="-5", font=("맑은 고딕", 25), command=click_button2)
button2.place(x=100,y=100,width=100,height=50)

button3 = Button(win, text="+10", font=("맑은 고딕", 25), command=click_button3)
button3.place(x=250,y=200,width=100,height=50)

button4 = Button(win, text="-10", font=("맑은 고딕", 25), command=click_button3)
button4.place(x=100,y=200,width=100,height=50)

win.geometry("400x400")
win.mainloop()


# pyinstaller -w -F --add-data '.\*.png;.' af_click.py