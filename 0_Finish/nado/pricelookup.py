import tkinter
from tkinter import *
import pandas as pd
from tkinter import messagebox

win = tkinter.Tk()
win.geometry("600x400")
win.title("Price Manager")

model = StringVar()
lens = StringVar()
temp = StringVar()
model_search = StringVar()

Calc_Frame = Frame(win)
Calc_Frame.pack(side=TOP)
Search_Frame = Frame(win)
Search_Frame.pack(side=TOP)

def get_price():
    df = pd.read_csv("Product_list.csv")
    number_of_items = len(df)

    for item in range(number_of_items):
        if item >=0:
            if str(df.iloc[item]['Product']) == str(ety_model.get()):
                model_price = int(df.iloc[item]['Price'])
                lbl_model2.configure(text=model_price)

    for item2 in range(number_of_items):
        if item2 >=0:
            if str(df.iloc[item2]['Product']) == str(ety_lens.get()):
                lens_price = int(df.iloc[item2]['Price'])
                lbl_lens2.configure(text=lens_price)

    if str(ety_temp.get()) == "high" or str(ety_temp.get()) == "medium":
        temp_price = 150
    else: temp_price = 0
    lbl_temp2.configure(text=temp_price)
    total_price = model_price+lens_price+temp_price
    lbl_price.configure(text=total_price)

def search_model():
    df = pd.read_csv("Product_list.csv")
    number_of_items = len(df)
    for item in range(number_of_items):
        if item >=0:
            if str(df.iloc[item]['Product']) == str(ety_model3.get()):
                model_price = str(df.iloc[item]['Price'])
                lbl_model_result.config(text="단가: "+model_price+" USD")
                break
            else:
                lbl_model_result.config(text="제품을 등록해주세요.")

def add_new():
    win_add=tkinter.Toplevel()
    win_add.geometry("300x300")
    win_add.title("Add new product")

    def add_new_product():
        ety_add_model.insert(0,model_search)
        df = pd.read_csv("Product_list.csv")
        m = ety_add_model.get()
        p = ety_add_price.get()
        df2 = pd.Series([m,p], index=["Product","Price"])
        df3 = df.append(df2, ignore_index=True)
        df3.to_csv("Product_list.csv", index=False)
        messagebox.showinfo("Info","제품이 정상적으로 등록되었습니다.")


    lbl_add_model=Label(win_add, text="Model",width=10).grid(row=0,column=0)
    lbl_add_price=Label(win_add, text="Price",width=10).grid(row=0,column=1)
    ety_add_model=Entry(win_add, text="",width=10)
    ety_add_model.grid(row=1,column=0)
    ety_add_price=Entry(win_add, text="",width=10)
    ety_add_price.grid(row=1,column=1)
    btn_insert=Button(win_add, text="Insert", width=10,command=add_new_product)
    btn_insert.grid(row=0, column=2)


    win_add.mainloop()
                      
lbl_model = Label(Calc_Frame, text="Model", width=10).grid(row=0, column=0)
lbl_lens = Label(Calc_Frame, text="Lens", width=10).grid(row=0, column=1)
lbl_temp = Label(Calc_Frame, text="Temp.", width=10).grid(row=0, column=2)
lbl_price = Label(Calc_Frame, text="", width=10)
lbl_price.grid(row=1, column=3)

lbl_model2 = Label(Calc_Frame, text="", width=10)
lbl_model2.grid(row=2, column=0)
lbl_lens2 = Label(Calc_Frame, text="", width=10)
lbl_lens2.grid(row=2, column=1)
lbl_temp2 = Label(Calc_Frame, text="", width=10)
lbl_temp2.grid(row=2, column=2)

ety_model = Entry(Calc_Frame, textvariable=model, width=10, justify=CENTER)
ety_model.grid(row=1,column=0)
ety_lens = Entry(Calc_Frame, textvariable=lens, width=10, justify=CENTER)
ety_lens.grid(row=1,column=1)
ety_temp = Entry(Calc_Frame, textvariable=temp, width=10, justify=CENTER)
ety_temp.grid(row=1,column=2)
btn_price = Button(Calc_Frame, text="Get price", command=get_price, width=10).grid(row=0, column=3)

lbl_model3 = Label(Search_Frame, text="Product", width=10).grid(row=3, column=0)
ety_model3 = Entry(Search_Frame, textvariable=model_search, width=10, justify=CENTER)
ety_model3.grid(row=3, column=1)
lbl_model_result = Label(Search_Frame, text="",width=20)
lbl_model_result.grid(row=3, column=2)
btn_search = Button(Search_Frame, text="Search", command=search_model, width=10).grid(row=3, column=3)
btn_add_new = Button(Search_Frame, text="Add", command=add_new, width=10).grid(row=3, column=4)

win.mainloop()