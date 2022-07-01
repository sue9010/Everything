import tkinter
from tkinter import StringVar, messagebox, Button, Entry,Label,Tk
from tkinter import font
from tkinter import Toplevel
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import os


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'")
options.add_argument('window-size=1920x1080')
options.add_argument('hide-scrollbars')
options.add_argument('disable-gpu')
options.add_argument("--log-level=3")
# options.add_argument('headless')

win = tkinter.Tk()
win.title("Unipass")
win.geometry("300x75")


label1 = Label(win, text= "시작일", font="arial")
label1.grid(row=0,column=0)
Entry1 = Entry(win)
Entry1.grid(row=0,column=1)
label2 = Label(win, text="종료일", font="arial")
label2.grid(row=1,column=0)
Entry2 = Entry(win)
Entry2.grid(row=1,column=1)

s_date = Entry1.get()
e_date = Entry2.get()

driver = webdriver.Chrome("E:\PythonPractice\chromedriver.exe", options=options)
wait = WebDriverWait(driver, 5)


def log_in():

    id = "coxcamera"
    pw = "Coxcamera3888##"
    pw2 = "coxcamera3880!!"

    driver = webdriver.Chrome("E:\PythonPractice\chromedriver.exe", options=options)
    driver.get('https://unipass.customs.go.kr/csp/openLogin.do')
    driver.maximize_window()
    pyautogui.sleep(0.5)
    driver.find_element_by_id('loginId').send_keys(id)
    pyautogui.sleep(0.5)
    driver.find_element_by_id('loginPwd').send_keys(pw)
    pyautogui.sleep(0.5)
    driver.find_element_by_id('BrwsAtdcLgnYn').click() # 금융인증서 로그인 체크박스
    driver.find_element_by_id('btnIdLgn').click() #로그인 버튼 클릭
    pyautogui.sleep(0.5)
    iframe = driver.find_element_by_id('dscert') #공인인증서 창으로 이동
    driver.switch_to.frame(iframe)
    pyautogui.sleep(3)
    driver.find_element_by_xpath('//*[@id="stg_hdd"]').click() #하드디스크, USB 클릭
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="hdd_driver_3"]/a').click() #K 드라이브 선택
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="row1dataTable"]/td[1]/span').click() #무역 공인인증서 선택
    pyautogui.sleep(1)        
    driver.find_element_by_xpath('//*[@id="input_cert_pw_new"]').send_keys(pw2) #비밀번호 입력창 선택
    pyautogui.sleep(1)     
    driver.find_element_by_xpath('//*[@id="btn_confirm_iframe"]').click() #로그인 버튼 클릭
    pyautogui.sleep(1)
    driver.minimize_window()
    win2 = tkinter.Toplevel()
    win2.geometry("300x300")
    win2.title("Command")


    def ept():
        driver.maximize_window()
        driver.find_element_by_link_text('전자신고').click() 
        driver.find_element_by_link_text('통관서식출력').click() 
        driver.find_element_by_link_text('수출신고필증').click()
        pyautogui.sleep(1)
        driver.find_element_by_xpath('//*[@id="MYC0112186S_acptStrtDt"]').click() #수리일자 체크박스 선택
        pyautogui.sleep(1)
        s_date = Entry1.get()
        e_date = Entry2.get()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').send_keys(s_date)
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').send_keys(e_date)
        driver.find_element_by_xpath('//*[@id="MYC0112186S_fmSearch_table"]/div/footer/button/span').click() #조회 버튼 클릭릭
        time.sleep(3)
        # wait.until(EC.element_to_be_selected((By.XPATH,'//*[@id="MYC0112186S_cb2_selector"]')))
        driver.implicitly_wait(60) 
        # wait.until(EC.presence_of_element_located((By.XPATH ,"//*[@id='YC0112186S_table']/tbody/tr[1]/td[3]/input")))
        # wait.until(EC.element_located_to_be_selected((By.XPATH ,'//*[@id="MYC0112186S_cb2_selector"]')))   
        # wait.until(EC.element_located_to_be_selected((By.XPATH ,'//*[@id="excelBtn"]')))
        # wait.until(EC.element_to_be_clickable((By.ID,'excelBtn')))     
        # wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="MYC0112186S_sorgPdfBtn"]')))        
        driver.find_element_by_id('MYC0112186S_cb2_selector').click() #필증 전체선택 체크박스
        driver.find_element_by_id('MYC0112186S_cb1_selector').click() #신고서 전체선택 체크박스
        driver.find_element_by_xpath('//*[@id="excelBtn"]/span').click()
        driver.find_element_by_xpath('//*[@id="MYC0112186S_sorgPdfBtn"]/span').click() #PDF 저장 버튼 클릭
        pyautogui.sleep(1)
        driver.implicitly_wait(10) 
        driver.switch_to.window(driver.window_handles[-1])
        # driver.implicitly_wait(10)  
        wait.until(EC.element_to_be_clickable((By.XPATH ,"//*[@id='MYC0112220S03_btnPdfDn']")))
        driver.find_element_by_xpath('//*[@id="MYC0112221S03_btnPdfDn"]').click()
        driver.implicitly_wait(10) 
        driver.switch_to.window(driver.window_handles[0])
        pyautogui.sleep(1)
        driver.implicitly_wait(10) 
        driver.find_element_by_id('MYC0112186S_prntBtn').click()
        driver.switch_to.window(driver.window_handles[-1]) #팝업창으로 이동
        driver.implicitly_wait(10)
        driver.find_element_by_id('ozMarkanyPrint').click() #인쇄버튼 클릭
        time.sleep(30)
        driver.switch_to.window(driver.window_handles[0])
        driver.minimize_window()
        messagebox.showinfo("Info","다운로드 완료")
    
    def ipt():
        driver.maximize_window()
        driver.find_element_by_link_text('전자신고').click() 
        driver.find_element_by_link_text('통관서식출력').click() 
        driver.find_element_by_link_text('수입신고필증').click()
        pyautogui.sleep(1)
        driver.find_element_by_xpath('//*[@id="MYC0112185S_acptStrtDt"]').click() #수리일자 체크박스 선택
        pyautogui.sleep(1)
        s_date = Entry1.get()
        e_date = Entry2.get()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').send_keys(s_date)
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').send_keys(e_date)
        driver.find_element_by_xpath('//*[@id="MYC0112185S_fmSearch_table"]/div/footer/button/span').click() #조회 버튼 클릭릭
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('//*[@id="MYC0112185S_cb2_selector"]').click() #필증 전체선택 체크박스
        driver.find_element_by_xpath('//*[@id="MYC0112185S_cb1_selector"]').click() #신고서 전체 선택 체크박스
        driver.find_element_by_xpath('//*[@id="excelBtn"]/span').click()
        driver.find_element_by_xpath('//*[@id="MYC0112185S_sorgPdfBtn"]/span').click() #PDF 저장 버튼 클릭
        pyautogui.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        pyautogui.sleep(5)
        driver.implicitly_wait(60)  
        driver.find_element_by_id('MYC0112220S03_btnPdfDn').click()
        pyautogui.sleep(10)
        driver.implicitly_wait(10) 
        pyautogui.sleep(10)
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(10) 
        pyautogui.sleep(10)
        driver.find_element_by_id('MYC0112185S_prntBtn').click()
        driver.switch_to.window(driver.window_handles[-1]) #팝업창으로 이동
        pyautogui.sleep(10)
        driver.implicitly_wait(10)
        driver.find_element_by_id('ozMarkanyPrint').click() #인쇄버튼 클릭
        time.sleep(30)
        driver.implicitly_wait(60)
        driver.switch_to.window(driver.window_handles[0])
        driver.minimize_window()
        messagebox.showinfo("Info","다운로드 완료")
    
    def one_shot():
        driver.maximize_window()
        driver.find_element_by_link_text('전자신고').click() 
        driver.find_element_by_link_text('통관서식출력').click() 
        driver.find_element_by_link_text('수출신고필증').click()
        pyautogui.sleep(1)
        driver.find_element_by_xpath('//*[@id="MYC0112186S_acptStrtDt"]').click() #수리일자 체크박스 선택
        pyautogui.sleep(1)
        s_date = Entry1.get()
        e_date = Entry2.get()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').send_keys(s_date)
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').send_keys(e_date)
        driver.find_element_by_xpath('//*[@id="MYC0112186S_fmSearch_table"]/div/footer/button/span').click() #조회 버튼 클릭릭
        time.sleep(5)
        driver.implicitly_wait(10) 
        driver.find_element_by_id('MYC0112186S_cb2_selector').click() #필증 전체선택 체크박스
        driver.find_element_by_id('MYC0112186S_cb1_selector').click() #신고서 전체선택 체크박스
        driver.find_element_by_xpath('//*[@id="excelBtn"]/span').click()
        driver.find_element_by_xpath('//*[@id="MYC0112186S_sorgPdfBtn"]/span').click() #PDF 저장 버튼 클릭
        pyautogui.sleep(1)
        driver.implicitly_wait(10) 
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(10)  
        driver.find_element_by_xpath('//*[@id="MYC0112221S03_btnPdfDn"]').click()
        driver.implicitly_wait(10) 
        driver.switch_to.window(driver.window_handles[0])
        pyautogui.sleep(1)
        driver.implicitly_wait(10) 
        driver.find_element_by_id('MYC0112186S_prntBtn').click()
        driver.switch_to.window(driver.window_handles[-1]) #팝업창으로 이동
        driver.implicitly_wait(10)
        driver.find_element_by_id('ozMarkanyPrint').click() #인쇄버튼 클릭
        time.sleep(30)
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_link_text('전자신고').click() 
        driver.find_element_by_link_text('통관서식출력').click() 
        driver.find_element_by_link_text('수입신고필증').click()
        pyautogui.sleep(1)
        driver.find_element_by_xpath('//*[@id="MYC0112185S_acptStrtDt"]').click() #수리일자 체크박스 선택
        pyautogui.sleep(1)
        s_date = Entry1.get()
        e_date = Entry2.get()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptStrtDt"]').send_keys(s_date)
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').clear()
        driver.find_element_by_xpath('//*[@id="acptEndDt"]').send_keys(e_date)
        driver.find_element_by_xpath('//*[@id="MYC0112185S_fmSearch_table"]/div/footer/button/span').click() #조회 버튼 클릭릭
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="MYC0112185S_cb2_selector"]').click() #필증 전체선택 체크박스
        driver.find_element_by_xpath('//*[@id="MYC0112185S_cb1_selector"]').click() #신고서 전체 선택 체크박스
        driver.find_element_by_xpath('//*[@id="excelBtn"]/span').click()
        driver.find_element_by_xpath('//*[@id="MYC0112185S_sorgPdfBtn"]/span').click() #PDF 저장 버튼 클릭
        pyautogui.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        pyautogui.sleep(5)
        driver.implicitly_wait(60)  
        driver.find_element_by_id('MYC0112220S03_btnPdfDn').click()
        pyautogui.sleep(10)
        driver.implicitly_wait(10) 
        pyautogui.sleep(10)
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(10) 
        pyautogui.sleep(10)
        driver.find_element_by_id('MYC0112185S_prntBtn').click()
        driver.switch_to.window(driver.window_handles[-1]) #팝업창으로 이동
        pyautogui.sleep(10)
        driver.implicitly_wait(10)
        driver.find_element_by_id('ozMarkanyPrint').click() #인쇄버튼 클릭
        time.sleep(30)
        driver.implicitly_wait(60)
        driver.switch_to.window(driver.window_handles[0])
        driver.minimize_window()
        messagebox.showinfo("Info","다운로드 완료")

    btn2 =Button(win2, text="Import", font="arial", command=ipt)
    btn2.pack()
    btn3 =Button(win2, text="Export", font="arial", command=ept)
    btn3.pack()
    btn3 =Button(win2, text="Oneshot", font="arial", command=one_shot)
    btn3.pack()
    win2.mainloop()
    
btn1 = Button(win, text="Login", font="arial", command=log_in)
btn1.grid(row=0,column=2)

win.mainloop()