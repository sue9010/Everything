import tkinter
import pandas as pd
from tkinter import *
from tkinter import ttk, messagebox

win = tkinter.Tk()

win.title("2021 출고")
win.geometry("1200x400")

frame_btn = Frame(win)
frame_btn.pack(side=RIGHT)
frame_insert = Frame(win)
frame_insert.pack(side=TOP)
frame_data = Frame(win)
frame_data.pack(side=BOTTOM)

def get_ety():
    ety1 = etys[0].get()
    ety2 = etys[1].get()
    ety3 = etys[2].get()
    ety4 = etys[3].get()
    ety5 = etys[4].get()
    ety6 = etys[5].get()
    ety7 = etys[6].get()
    ety8 = etys[7].get()
    ety9 = etys[8].get()
    ety10 = etys[9].get()
    ety11 = etys[10].get()
    ety12 = etys[11].get()
    ety13 = etys[12].get()

def get_df():
    df.at[frow,"NUM"]=ety1
    df.at[frow,"출고일"]=ety2
    df.at[frow,"문서명"]=ety3
    df.at[frow,"구분"]=ety4
    df.at[frow,"업체명"]=ety5
    df.at[frow,"모델명"]=ety6
    df.at[frow,"해상도"]=ety7
    df.at[frow,"렌즈"]=ety8
    df.at[frow,"온도"]=ety9
    df.at[frow,"기타옵션"]=ety10
    df.at[frow,"S/N"]=ety11
    df.at[frow,"수량"]=ety12
    df.at[frow,"노트"]=ety13    

def insert_data():
    frow=df.head(1).index[0]
    get_ety()
    # ety1 = etys[0].get()
    # ety2 = etys[1].get()
    # ety3 = etys[2].get()
    # ety4 = etys[3].get()
    # ety5 = etys[4].get()
    # ety6 = etys[5].get()
    # ety7 = etys[6].get()
    # ety8 = etys[7].get()
    # ety9 = etys[8].get()
    # ety10 = etys[9].get()
    # ety11 = etys[10].get()
    # ety12 = etys[11].get()
    # ety13 = etys[12].get()
    # df.at[frow,"NUM"]=ety1
    # df.at[frow,"출고일"]=ety2
    # df.at[frow,"문서명"]=ety3
    # df.at[frow,"구분"]=ety4
    # df.at[frow,"업체명"]=ety5
    # df.at[frow,"모델명"]=ety6
    # df.at[frow,"해상도"]=ety7
    # df.at[frow,"렌즈"]=ety8
    # df.at[frow,"온도"]=ety9
    # df.at[frow,"기타옵션"]=ety10
    # df.at[frow,"S/N"]=ety11
    # df.at[frow,"수량"]=ety12
    # df.at[frow,"노트"]=ety13
    trv.insert("",frow,values=(ety1,ety2,ety3,ety4,ety5,ety6,ety7,ety8,ety9,ety10,ety11,ety12,ety13))
    for x in etys:
        x.delete(0,END)
    df.to_excel('2021.xlsx', index=FALSE)

def delete_data():
    selected_item = trv.selection()[0]
    idx=trv.index(selected_item)
    trv.delete(selected_item)
    df.drop(idx, inplace=True)
    df.to_excel('2021.xlsx', index=FALSE)

    
btn =Button(frame_btn, text="insert", command=insert_data, width=10)
btn.pack()
btn2 =Button(frame_btn, text="delete", command=delete_data, width=10)
btn2.pack()
lbl11 = Label(frame_insert, width=10, text="NUM").grid(row=0, column=0)
lbl12 = Label(frame_insert, width=10, text="출고일").grid(row=0, column=1)
lbl13 = Label(frame_insert, width=10, text="문서명").grid(row=0, column=2)
lbl14 = Label(frame_insert, width=10, text="구분").grid(row=0, column=3)
lbl15 = Label(frame_insert, width=10, text="업체명").grid(row=0, column=4)
lbl16 = Label(frame_insert, width=10, text="모델명").grid(row=0, column=5)
lbl17 = Label(frame_insert, width=10, text="해상도").grid(row=0, column=6)
lbl18 = Label(frame_insert, width=10, text="렌즈").grid(row=0, column=7)
lbl19 = Label(frame_insert, width=10, text="온도").grid(row=0, column=8)
lbl110 = Label(frame_insert, width=10, text="기타옵션").grid(row=0, column=9)
lbl111 = Label(frame_insert, width=10, text="S/N").grid(row=0, column=10)
lbl112 = Label(frame_insert, width=10, text="수량").grid(row=0, column=11)
lbl113 = Label(frame_insert, width=10, text="노트").grid(row=0, column=12)

etys =[]
for y in range(13):
    ety = Entry(frame_insert, width=10)
    ety.grid(row=1, column=y)
    etys.append(ety)

df = pd.read_excel('2021.xlsx')
trv = ttk.Treeview(frame_data, height=18)
trv["column"]=list(df.columns)
trv["show"]="headings"
# lbl_lists = ["Num", "출고일", "문서명", "구분", "업체명", "모델명","해상도", "렌즈", "온도", "기타옵션", "S/N", "수량","노트"]
w = 75
trv.column("NUM",width=w)
trv.column("출고일",width=w)
trv.column("문서명",width=w)
trv.column("구분",width=w)
trv.column("업체명",width=w)
trv.column("모델명",width=w)
trv.column("해상도",width=w)
trv.column("렌즈",width=w)
trv.column("온도",width=w)
trv.column("기타옵션",width=w)
trv.column("S/N",width=w)
trv.column("수량",width=w)
trv.column("노트",width=w)

for column in trv["columns"]:
    trv.heading(column, text=column)
df_rows = df.to_numpy().tolist()

for row in df_rows:
    trv.insert("","end",values=row)

trv.pack()

win.mainloop()