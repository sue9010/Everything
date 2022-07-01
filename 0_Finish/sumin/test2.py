import tkinter 
from tkinter import *
from tkinter import messagebox
import pandas as pd
import os
from openpyxl import load_workbook
# import pdfkit
# from pdfkit.api import configuration


main_win = tkinter.Tk()
main_win.geometry("200x100")
options = {'quiet': ''}    
# config = pdfkit.configuration(wkhtmltopdf=r'E:\PythonPractice\bin\wkhtmltopdf.exe')
itemnum = IntVar()
ordernum = StringVar()
orderdate= StringVar()

def add_order():
#==========================================window size=======================================#
    itemnums = int(ety_n.get())
    sub_window = tkinter.Toplevel()
    height = itemnums * 40 +20
    if itemnums >= 4:
        sub_window.geometry("700x%d" % (height))
    else:
        sub_window.geometry("700x180")
#==========================================frames=============================================#
    frame_info = Frame(sub_window)
    frame_info.pack(side=TOP)
    frame_btn = Frame(sub_window)
    frame_btn.pack(side=RIGHT)
    frame_insert = Frame(sub_window)
    frame_insert.pack()
    frame_output = Frame(sub_window)
    frame_output.pack(side=BOTTOM)
#======================================variables===========================================# 
    x=0
    etys = []
    b = []
    labels = ["Model", "Lens","Temp", "Qty", "Unit Price", "Amount"]
    lbl_count = len(labels)
    ordernumber = ety_o.get()
    orderdates= ety_d.get()
#======================================make entries===========================================# 
    while x < lbl_count:
        for lbl in labels:
            lbl = Label(frame_insert, text=lbl, width=10)
            lbl.grid(row=0,column=x)
            x += 1
    for y in range(itemnums):
        for x in range(lbl_count):
            ety = Entry(frame_insert, width=10)
            ety.grid(row=y+1, column=x, padx=10, pady=10)
            etys.append(ety)
#======================================make labels===========================================# 
    lbl_order_number = Label(frame_btn, text="발주번호: "+ordernumber)
    lbl_order_number.pack()
    lbl_order_date = Label(frame_btn, text="발주날짜: "+orderdates)
    lbl_order_date.pack()

    lbl = Label(frame_btn, text='', width=20)
    lbl.pack()
    lbl2 = Label(frame_output, text='')
    lbl2.grid(row=0, column=0)
#======================================make functions=========================================# 
  
    def list_chunk(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]

    def clear():
        for x in range(itemnums*lbl_count):
            etys[x].delete(0,END)

    def show():
        calc()
        calc()

    def calc():
        for x in range(itemnums*lbl_count):
            if not etys[x].get():
                etys[x].insert(0,0)
            else:
                if (x+1) % lbl_count ==0:
                    etys[x].delete(0,END)
                    etys[x].insert(0,(int(etys[x-2].get()))*(int(etys[x-1].get())))
        for y in range(itemnums*lbl_count):
            if y % lbl_count == 0:
                a = int(etys[y-1].get())
                b.append(a)
        c = sum(b)
        b.clear()
        lbl.config(text="Total: "+str(c))
 
    def save_data():
        et = []
        for x in range(itemnums*lbl_count):
            e = etys[x].get()
            et.append(e)

        df = pd.read_excel('df2.xlsx')
        df2 = pd.DataFrame(list_chunk(et, lbl_count), columns=["Model","Lens","Temp", "Qty","Unit Price","Amount"])
        df3 = pd.concat([df, df2])
        df3.to_excel("df2.xlsx", index=False)
        df3.to_html("df2.html", index=False, col_space='75px')

        messagebox.showinfo("INFO","저장 완료")

    def print_data():
        pdfkit.from_file('df2.html','df2.pdf', options=options, configuration=config)
        os.startfile("df2.pdf","print")

#======================================make buttons===========================================#
    btn1 = Button(frame_btn, text="clear", width=10, command=clear).pack()
    btn2 = Button(frame_btn, text="show", width=10, command=show).pack()
    btn3 = Button(frame_btn, text="save", width=10, command=save_data).pack()
    btn4 = Button(frame_btn, text="print", width=10, command=print_data).pack()
    sub_window.mainloop()

lbl_n = Label(main_win, text="아이템 수", width=10).grid(row=0,column=0)
ety_n = Entry(main_win, textvariable=itemnum, width=10)
ety_n.grid(row=0, column=1)
lbl_o = Label(main_win, text="발주번호", width=10).grid(row=1,column=0)
ety_o = Entry(main_win, textvariable=ordernum, width=10)
ety_o.grid(row=1, column=1)
lbl_d = Label(main_win, text="발주날짜", width=10).grid(row=2,column=0)
ety_d = Entry(main_win, textvariable=orderdate, width=10)
ety_d.grid(row=2, column=1)

btn = Button(main_win, text="ADD", command= add_order).grid(row=0, column=3)

main_win.mainloop()