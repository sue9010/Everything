import tkinter
from tkinter import messagebox, Button, Entry,Label,Tk
import pyautogui
from selenium import webdriver




win = tkinter.Tk()
win.title("Unipass")
win.geometry("400x75")

id = "coxcamera"
pw = "Coxcamera3888##"
pw2 = "coxcamera3880!!"

def import_d():
    driver = webdriver.Chrome("E:\PythonPractice\chromedriver.exe")
    driver.get('https://unipass.customs.go.kr/csp/openLogin.do')
    driver.maximize_window()
    driver.find_element_by_id('loginId').send_keys(id)
    pyautogui.sleep(0.5)
    driver.find_element_by_id('loginPwd').send_keys(pw)
    pyautogui.sleep(0.5)
    driver.find_element_by_id('BrwsAtdcLgnYn').click() # 금융인증서 로그인 체크박스
    driver.find_element_by_id('btnIdLgn').click() #로그인 버튼 클릭
    iframe = driver.find_element_by_id('dscert') #공인인증서 창으로 이동
    driver.switch_to.frame(iframe)
    pyautogui.sleep(3)
    driver.find_element_by_xpath('//*[@id="stg_hdd"]').click() #하드디스크, USB 클릭
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="hdd_driver_6"]/a').click() #K 드라이브 선택
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="row1dataTable"]/td[1]/span').click() #무역 공인인증서 선택
    pyautogui.sleep(1)        
    driver.find_element_by_xpath('//*[@id="input_cert_pw_new"]').send_keys(pw2) #비밀번호 입력\
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="btn_confirm_iframe"]/span').click() #로그인 버튼 클릭
    pyautogui.sleep(5)
    driver.find_element_by_xpath('//*[@id="topmenu"]/ul/li[2]/a/span').click()
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="selA_MYC_MNU_00000058"]/span').click()
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="beforeWeekBtn"]').click()
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="MYC0115001Q_brno"]').click()
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="MYC0115001Q_fmSearch_table"]/div/footer/button/span').click()
    pyautogui.sleep(1)
    driver.find_element_by_xpath('//*[@id="MYC0115001Q_table"]/tbody/tr[1]/td[5]/a').click()
    pyautogui.sleep(1)
    print(driver.find_element_by_xpath('//*[@id="MYC0101001S_byerConm"]').get_attribute("value"))



Button2= Button(win, text= "수입신고필증", command = import_d, font="arial")
Button2.grid(row=0,column=3)


win.mainloop()