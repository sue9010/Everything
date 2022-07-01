import tkinter
from openpyxl import workbook
import pandas as pd
from tkinter import *
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk, ThemedStyle, themed_style
import openpyxl
from win32com import client
import win32api

win = tkinter.Tk()
# win = ThemedTk(theme = 'black')
win.title("Buyer Information")
win.geometry("710x400")

mainFrame= Frame(win)
# mainFrame= Frame(win, padx=10, pady=10)
mainFrame.pack(side=LEFT, fill=Y, expand=1)

infoFrame = Frame(win)
# infoFrame = Frame(leftFrame, padx=10, pady=10, highlightbackground="silver", highlightcolor="silver", highlightthickness=2)
infoFrame.pack(side=RIGHT)

btnFrame=Frame(infoFrame)
btnFrame.grid(row=15, column=1)

df = pd.read_excel('company.xlsx')

t_scroll = Scrollbar(mainFrame)
t_scroll.pack(side=RIGHT, fill=Y)

trv = ttk.Treeview(mainFrame, yscrollcommand=t_scroll.set, height=18)

trv["column"]=list(df.columns[:2])
trv["show"]="headings"

t_scroll.config(command=trv.yview)

trv.column("Num",width=40)
trv.column("업체명",width=200)
for column in trv["columns"]:
    trv.heading(column, text=column)
df_rows = df.to_numpy().tolist()

for row in df_rows:
    trv.insert("","end",values=row)

trv.pack()
#=================================================================================================
num=StringVar()
c_num=StringVar()
c_name= StringVar()
shc= StringVar()
note= StringVar()
tp_mth= StringVar()
tp_acc= StringVar()
ep_date= StringVar()
ep_num= StringVar()
ep_license= StringVar()
email= StringVar()
tel= StringVar()
attn= StringVar()
address= StringVar()
ct_sort= StringVar()
ct_name= StringVar()

h_list = "Num","업체명","국가","국가 분류","주소","담당자","전화번호","이메일","수출허가","수출허가번호","수출허가 만료일","운송계정","운송방법", "업체별 특이사항","단축어"
sc_list=num,c_name,ct_name,ct_sort,address,attn,tel,email,ep_license,ep_num,ep_date,tp_acc,tp_mth,note,shc
# ety_list=ety1.get(),ety2.get(),ety3.get(),ety4.get(),ety5.get(),ety6.get(),ety7.get(),ety8.get(),ety9.get(),ety10.get(),ety11.get(),ety12.get(),ety13.get(),ety14.get(),ety15.get()
#=======================================Functions===========================================
def get_ety():
    num=ety1.get()
    c_name=ety2.get()
    ct_name=ety3.get()
    ct_sort=ety4.get()
    address=ety5.get()
    attn=ety6.get()
    tel=ety7.get()
    email=ety8.get()
    ep_license=ety9.get()
    ep_num=ety10.get()
    ep_date=ety11.get()
    tp_acc=ety12.get()
    tp_mth=ety13.get()
    note=ety14.get()
    shc=ety15.get()
    # ety_list=ety1.get(),ety2.get(),ety3.get(),ety4.get(),ety5.get(),ety6.get(),ety7.get(),ety8.get(),ety9.get(),ety10.get(),ety11.get(),ety12.get(),ety13.get(),ety14.get(),ety15.get()

def show_data():
    trv.delete(*trv.get_children())
    df = pd.read_excel('company.xlsx')
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        trv.insert("","end",values=row)

def selectItem(a):
    curitem = trv.focus()
    q = trv.item(curitem).get("values")
    ety1.delete(0, END)
    ety2.delete(0, END)
    ety3.delete(0, END)
    ety4.delete(0, END)
    ety5.delete(0, END)
    ety6.delete(0, END)
    ety7.delete(0, END)
    ety8.delete(0, END)
    ety9.delete(0, END)
    ety10.delete(0, END)
    ety11.delete(0, END)
    ety12.delete(0, END)
    ety13.delete(0, END)
    ety14.delete(0, END)
    ety15.delete(0, END)

    num=q[0]
    c_name=q[1]
    ct_name=q[2]
    ct_sort=q[3]
    address=q[4]
    attn=q[5]
    tel=q[6]
    email=q[7]
    ep_license=q[8]
    ep_num=q[9]
    ep_date=q[10]
    tp_acc=q[11]
    tp_mth=q[12]
    note=q[13]
    shc=q[14]

    ety1.insert(0,num)
    ety2.insert(0,c_name)
    ety3.insert(0,ct_name)
    ety4.insert(0,ct_sort)
    ety5.insert(0,address)
    ety6.insert(0,attn)
    ety7.insert(0,tel)
    ety8.insert(0,email)
    ety9.insert(0,ep_license)
    ety10.insert(0,ep_num)
    ety11.insert(0,ep_date)
    ety12.insert(0,tp_acc)
    ety13.insert(0,tp_mth)
    ety14.insert(0,note)
    ety15.insert(0,shc)

def search_data(e):
    pass

def add_new():
    rows=df.tail(1).index[0]
    nrow = rows+1
    num=ety1.get()
    c_name=ety2.get()
    ct_name=ety3.get()
    ct_sort=ety4.get()
    address=ety5.get()
    attn=ety6.get()
    tel=ety7.get()
    email=ety8.get()
    ep_license=ety9.get()
    ep_num=ety10.get()
    ep_date=ety11.get()
    tp_acc=ety12.get()
    tp_mth=ety13.get()
    note=ety14.get()
    shc=ety15.get()
    df.at[nrow,("Num","업체명","국가","국가 분류","주소","담당자","전화번호","이메일","수출허가","수출허가번호","수출허가 만료일","운송계정","운송방법", "업체별 특이사항","단축어")]=(num,c_name,ct_name,ct_sort,address,attn,tel,email,ep_license,ep_num,ep_date,tp_acc,tp_mth,note,shc)
    trv.insert(parent='', index='end', text="", values=(num,c_name,ct_name,ct_sort,address,attn,tel,email,ep_license,ep_num,ep_date,tp_acc,tp_mth,note,shc))
    ety1.delete(0, END)
    ety2.delete(0, END)
    ety3.delete(0, END)
    ety4.delete(0, END)
    ety5.delete(0, END)
    ety6.delete(0, END)
    ety7.delete(0, END)
    ety8.delete(0, END)
    ety9.delete(0, END)
    ety10.delete(0, END)
    ety11.delete(0, END)
    ety12.delete(0, END)
    ety13.delete(0, END)
    ety14.delete(0, END)
    ety15.delete(0, END)
    df.to_excel('company.xlsx', index=False)
    messagebox.showinfo("Info", "데이터가 성공적으로 추가되었습니다.")

def change_data():
    selected_item = trv.selection()[0]
    idx=trv.index(selected_item)
    num=ety1.get()
    c_name=ety2.get()
    ct_name=ety3.get()
    ct_sort=ety4.get()
    address=ety5.get()
    attn=ety6.get()
    tel=ety7.get()
    email=ety8.get()
    ep_license=ety9.get()
    ep_num=ety10.get()
    ep_date=ety11.get()
    tp_acc=ety12.get()
    tp_mth=ety13.get()
    note=ety14.get()
    shc=ety15.get()
    selected = trv.focus()
    trv.item(selected, text="", values=(num,c_name,ct_name,ct_sort,address,attn,tel,email,ep_license,ep_num,ep_date,tp_acc,tp_mth,note,shc))
    df.at[idx,("Num","업체명","국가","국가 분류","주소","담당자","전화번호","이메일","수출허가","수출허가번호","수출허가 만료일","운송계정","운송방법", "업체별 특이사항","단축어")]=(num,c_name,ct_name,ct_sort,address,attn,tel,email,ep_license,ep_num,ep_date,tp_acc,tp_mth,note,shc)
    ety1.delete(0, END)
    ety2.delete(0, END)
    ety3.delete(0, END)
    ety4.delete(0, END)
    ety5.delete(0, END)
    ety6.delete(0, END)
    ety7.delete(0, END)
    ety8.delete(0, END)
    ety9.delete(0, END)
    ety10.delete(0, END)
    ety11.delete(0, END)
    ety12.delete(0, END)
    ety13.delete(0, END)
    ety14.delete(0, END)
    ety15.delete(0, END)
    df.to_excel('company.xlsx', index=False)
    messagebox.showinfo("Info", "수정이 완료되었습니다.")

def delete_data():
    res = messagebox.askyesno("Info","데이터를 정말 삭제하시겠습니까?")
    if res == YES:
        selected_item = trv.selection()[0]
        idx=trv.index(selected_item)
        trv.delete(selected_item)
        df.drop(idx, inplace=True)
        df.to_excel('company.xlsx', index=FALSE)
        messagebox.showinfo("Info", "데이터가 성공적으로 삭제되었습니다.")
    else:
        messagebox.showinfo("Info","작업이 취소되었습니다.")

def clear_data():
    ety1.delete(0, END)
    ety2.delete(0, END)
    ety3.delete(0, END)
    ety4.delete(0, END)
    ety5.delete(0, END)
    ety6.delete(0, END)
    ety7.delete(0, END)
    ety8.delete(0, END)
    ety9.delete(0, END)
    ety10.delete(0, END)
    ety11.delete(0, END)
    ety12.delete(0, END)
    ety13.delete(0, END)
    ety14.delete(0, END)
    ety15.delete(0, END)

def save_data():
    df.to_excel('company.xlsx', index=False)

    messagebox.showinfo("INFO","저장 완료!")

def get_last_row():
    rows=df.tail(1)
    lrow = rows['Num'].values

    new_row = lrow + 1
    ety1.delete(0, END)
    num=new_row[0]
    ety1.insert(0,num)

def tempp(event):
    win_o = tkinter.Tk()
    win_o.geometry("800x400")
    win_o.title("Orders")

    frame_buyer = Frame(win_o)
    frame_buyer.pack(side=LEFT)
    frame_order = Frame(win_o)
    frame_order.pack(side=LEFT)
    frame_btn = Frame(win_o)
    frame_btn.pack(side=RIGHT)

    lbl1 = Label(frame_buyer, text="업체명:  " +ety2.get(), anchor=W)
    lbl2 = Label(frame_buyer, text="담당자:  " +ety6.get(), anchor=W)
    lbl3 = Label(frame_buyer, text="연락처:  " +ety7.get(), anchor=W)
    lbl4 = Label(frame_buyer, text="주  소:  " +ety5.get(), anchor=W, wraplength =300)
    lbl1.pack(side=TOP)
    lbl2.pack(side=TOP)
    lbl3.pack(side=TOP)
    lbl4.pack(side=TOP)

    def printt():
        input_file = r'E:\PythonPractice\quotation.xlsx'
        #give your file name with valid path 
        output_file = r'E:\PythonPractice\quotation.pdf'
        #give valid output file name and path
        app = client.DispatchEx("Excel.Application")
        app.Interactive = False
        app.Visible = False
        Workbook = app.Workbooks.Open(input_file)
        try:
            Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
        except Exception as e:
            print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
            print(str(e))
        finally:
            Workbook.Close()
            app.Exit()
    
 
    df = pd.read_excel(ety2.get()+".xlsx")
    t_scroll = Scrollbar(frame_buyer)
    t_scroll.pack(side=RIGHT, fill=Y)
    trv = ttk.Treeview(frame_buyer, yscrollcommand=t_scroll.set, height=18)
    trv["column"]=list(df.columns[:3])
    trv["show"]="headings"
    t_scroll.config(command=trv.yview)
    for column in trv["columns"]:
        trv.heading(column, text=column)
    df_rows = df.to_numpy().tolist()
    trv.column("발주번호",width=100)
    trv.column("발주날짜",width=75)
    trv.column("발주총액",width=120,anchor=E)
    for row in df_rows:
        trv.insert("","end",values=row)
    trv.pack(side=LEFT)
    # selected_item = trv.selection()[1]
    # idx=trv.index(selected_item)
    def temppp():
        win_temp= tkinter.Tk()
        win_temp.geometry("400x400")
        df = pd.read_excel(ety2.get()+".xlsx")
        t_scroll = Scrollbar(frame_buyer)
        t_scroll.pack(side=RIGHT, fill=Y)
        trv = ttk.Treeview(frame_buyer, yscrollcommand=t_scroll.set, height=18)
        trv["column"]=list(df.columns[:3])
        trv["show"]="headings"
        t_scroll.config(command=trv.yview)
        for column in trv["columns"]:
            trv.heading(column, text=column)
        df_rows = df.to_numpy().tolist()
        trv.column("발주번호",width=100)
        trv.column("발주날짜",width=75)
        trv.column("발주총액",width=120,anchor=E)
        for row in df_rows:
            trv.insert("","end",values=row)
        trv.pack(side=LEFT)
        win.mainloop()

    def calc():
        ety_am1.insert(0,int(ety_qty1.get())+int(ety_up1.get()))
        ety_am2.insert(0,int(ety_qty2.get())+int(ety_up2.get()))
        ety_total.insert(0,int(ety_am1.get())+int(ety_am2.get()))

    model1 = StringVar()
    lens1 =StringVar()
    temp1 = StringVar()
    qty1 = IntVar()
    up1 = IntVar()
    am1 = IntVar()

    model2 = StringVar()
    lens2 =StringVar()
    temp2 = StringVar()
    qty2 = IntVar()
    up2 = IntVar()
    am2 = IntVar()

    totalamount = IntVar()
    
    lbl_model = Label(frame_order, text="모델", width=10).grid(row=0, column=0)
    lbl_lens = Label(frame_order, text="렌즈", width=10).grid(row=0, column=1)
    lbl_temp = Label(frame_order, text="온도", width=10).grid(row=0, column=2)
    lbl_qty = Label(frame_order, text="수량", width=10).grid(row=0, column=3)
    lbl_up = Label(frame_order, text="단가", width=10).grid(row=0, column=4)
    lbl_am = Label(frame_order, text="금액", width=10).grid(row=0, column=5)

    ety_model1 = Entry(frame_order, textvariable=model1, width=10).grid(row=1,column=0)
    ety_lens1 = Entry(frame_order, textvariable=lens1, width=10).grid(row=1,column=1)
    ety_temp1 = Entry(frame_order, textvariable=temp1, width=10).grid(row=1,column=2)
    ety_qty1 = Entry(frame_order, textvariable=qty1, width=10)
    ety_up1 = Entry(frame_order, textvariable=up1, width=10)
    ety_am1 = Entry(frame_order, textvariable=am1, width=10)

    ety_qty1.grid(row=1,column=3)
    ety_up1.grid(row=1,column=4)
    ety_am1.grid(row=1, column=5)

    ety_model2 = Entry(frame_order, textvariable=model2, width=10).grid(row=2,column=0)
    ety_lens2 = Entry(frame_order, textvariable=lens2, width=10).grid(row=2,column=1)
    ety_temp2 = Entry(frame_order, textvariable=temp2, width=10).grid(row=2,column=2)
    ety_qty2 = Entry(frame_order, textvariable=qty2, width=10)
    ety_up2 = Entry(frame_order, textvariable=up2, width=10)
    ety_am2 = Entry(frame_order, textvariable=am2, width=10)
    
    ety_qty2.grid(row=2,column=3)
    ety_up2.grid(row=2,column=4)
    ety_am2.grid(row=2, column=5)

    ety_total = Entry(frame_order, textvariable=totalamount, width=10)
    ety_total.grid(row=3, column=5)

    btn_cal = Button(frame_btn, text="Calc", command=calc)
    btn_cal.pack()
    btn = Button(frame_btn, text="Print", command=printt)
    btn.pack()
    btn_show = Button(frame_btn, text="show", command=temppp)
    btn_show.pack()
    
    trv.bind("<Double-1>", tempp)

    win_o.mainloop()
    

trv.bind("<Double-1>", tempp)
trv.bind('<ButtonRelease-1>', selectItem)
#=======================================Label&Entry&Button===========================================
lbl1=Label(infoFrame,text="번호",width=12,anchor=E)
lbl2=Label(infoFrame,text="업체명",width=12,anchor=E)
lbl3=Label(infoFrame,text="국가명",width=12,anchor=E)
lbl4=Label(infoFrame,text="국가분류",width=12,anchor=E)
lbl5=Label(infoFrame,text="주소",width=12,anchor=E)
lbl6=Label(infoFrame,text="담당자",width=12,anchor=E)
lbl7=Label(infoFrame,text="전화번호",width=12,anchor=E)
lbl8=Label(infoFrame,text="이메일",width=12,anchor=E)
lbl9=Label(infoFrame,text="수출허가",width=12,anchor=E)
lbl10=Label(infoFrame,text="수출허가번호",width=12,anchor=E)
lbl11=Label(infoFrame,text="수출허가만료일",width=12,anchor=E)
lbl12=Label(infoFrame,text="운송 계정",width=12,anchor=E)
lbl13=Label(infoFrame,text="운송 방법",width=12,anchor=E)
lbl14=Label(infoFrame,text="특이사항",width=12,anchor=E)
lbl15=Label(infoFrame,text="단축어",width=12,anchor=E)
# "번호","업체명","국가명","국가분류","주소","담당자","전화번호","이메일","수출허가","수출허가번호","수출허가만료일","운송 계정","운송 방법","특이사항","단축어"
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=0)
lbl3.grid(row=2,column=0)
lbl4.grid(row=3,column=0)
lbl5.grid(row=4,column=0)
lbl6.grid(row=5,column=0)
lbl7.grid(row=6,column=0)
lbl8.grid(row=7,column=0)
lbl9.grid(row=8,column=0)
lbl10.grid(row=9,column=0)
lbl11.grid(row=10,column=0)
lbl12.grid(row=11,column=0)
lbl13.grid(row=12,column=0)
lbl14.grid(row=13,column=0)
lbl15.grid(row=14,column=0)

ety1=Entry(infoFrame,textvariable=num,width=50)
ety2=Entry(infoFrame,textvariable=c_name,width=50)
ety3=Entry(infoFrame,textvariable=ct_name,width=50)
ety4=Entry(infoFrame,textvariable=ct_sort,width=50)
ety5=Entry(infoFrame,textvariable=address,width=50)
ety6=Entry(infoFrame,textvariable=attn,width=50)
ety7=Entry(infoFrame,textvariable=tel,width=50)
ety8=Entry(infoFrame,textvariable=email,width=50)
ety9=Entry(infoFrame,textvariable=ep_license,width=50)
ety10=Entry(infoFrame,textvariable=ep_num,width=50)
ety11=Entry(infoFrame,textvariable=ep_date,width=50)
ety12=Entry(infoFrame,textvariable=tp_acc,width=50)
ety13=Entry(infoFrame,textvariable=tp_mth,width=50)
ety14=Entry(infoFrame,textvariable=note,width=50)
ety15=Entry(infoFrame,textvariable=shc,width=50)


ety1.grid(row=0,column=1)
ety2.grid(row=1,column=1)
ety3.grid(row=2,column=1)
ety4.grid(row=3,column=1)
ety5.grid(row=4,column=1)
ety6.grid(row=5,column=1)
ety7.grid(row=6,column=1)
ety8.grid(row=7,column=1)
ety9.grid(row=8,column=1)
ety10.grid(row=9,column=1)
ety11.grid(row=10,column=1)
ety12.grid(row=11,column=1)
ety13.grid(row=12,column=1)
ety14.grid(row=13,column=1)
ety15.grid(row=14,column=1)

btn9=Button(btnFrame,text="신규",width=10,anchor=CENTER, command=get_last_row)
btn3=Button(btnFrame,text="조회",width=10,anchor=CENTER,command=search_data)
btn4=Button(btnFrame,text="추가",width=10,anchor=CENTER,command=add_new)
btn5=Button(btnFrame,text="수정",width=10,anchor=CENTER,command=change_data)
btn6=Button(btnFrame,text="삭제",width=10,anchor=CENTER,command=delete_data)
btn7=Button(btnFrame,text="비우기",width=10,anchor=CENTER,command=clear_data)
btn10=Button(btnFrame,text="임시",width=10,anchor=CENTER, command=tempp)

btn9.grid(row=0,column=0)
btn3.grid(row=0,column=1)

btn4.grid(row=0,column=2)
btn5.grid(row=1,column=0)
btn6.grid(row=1,column=1)
btn7.grid(row=1,column=2)
btn10.grid(row=1,column=3)

win.mainloop()