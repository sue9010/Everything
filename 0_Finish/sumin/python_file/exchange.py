import tkinter
from tkinter import messagebox, Button, Entry,Label,Tk
import openpyxl
import pyautogui
from selenium import webdriver
import time
from openpyxl import *

win = tkinter.Tk()
win.title("환율")
win.geometry("220x50")
win.resizable(0,0)

label1= Label(win, text="시작일")
label1.grid(row=0,column=0)
label2= Label(win, text="종료일")
label2.grid(row=1,column=0)
ety1 = Entry(win, textvariable="s_date")
ety1.grid(row=0,column=1)
ety2 = Entry(win, textvariable="e_date")
ety2.grid(row=1,column=1)

def get_exchange():
    s_date = ety1.get()
    e_date = ety2.get()

    a=int(ety1.get())
    b=int(ety2.get())+1

    if a>=b:
        messagebox.showerror("경고!", "종료일이 시작일보다 작습니다.")
    else:
        wb = openpyxl.Workbook()
        ws = wb.active

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'")
        options.add_argument('window-size=1920x1080')
        options.add_argument('hide-scrollbars')
        options.add_argument('disable-gpu')
        options.add_argument("--log-level=3")

        driver = webdriver.Chrome("E:\PythonPractice\chromedriver.exe", options=options)
        driver.get('https://unipass.customs.go.kr/csp/index.do')
        driver.maximize_window()
        time.sleep(2)

        pyautogui.click(308,479)
        driver.implicitly_wait(5)

        for i in range (a,b):
            
            driver.find_element_by_id('MYC0401004Q_aplyDt').clear()
            driver.find_element_by_id('MYC0401004Q_aplyDt').send_keys(i)
            driver.find_element_by_xpath('//*[@id="MYC0401004Q_frmlForm"]/div/footer/button/span').click()
            driver.implicitly_wait(20)
            elem = driver.find_element_by_xpath('//*[@id="MYC0401004Q_table1"]/tbody/tr[57]/td[4]')

            ws.append([i, elem.text])

        file_name = s_date+"~"+e_date+"환율.xlsx"
        wb.save(file_name)
        driver.quit()
        messagebox.showinfo("완료","완료")

btn = Button(win, text="Run", command=get_exchange)
btn.grid(row=0,column=2)

win.mainloop()

