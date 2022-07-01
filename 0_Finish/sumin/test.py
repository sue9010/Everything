from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Counter
import mysql.connector

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def search():
    q2 = ent.get()
    query = "SELECT id, first_name, last_name, age FROM customers where first_name LIKE '%"+q2+"%' or last_name LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows= cursor.fetchall()
    update(rows)

def clear():
    query ="SELECT id, first_name, last_name, age FROM customers"
    cursor.execute(query)
    rows= cursor.fetchall()
    update(rows)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    values = trv.item(item, 'values')
    t1.insert(0, values[0])
    t2.insert(0, values[1])
    t3.insert(0, values[2])
    t4.insert(0, values[3])

    # t1.set(item["values"][0])
    # t2.set(item["values"][1])
    # t3.set(item["values"][2])
    # t4.set(item["values"][3])

def update_customer():
    return True

def add_new():
    global count

    #     ent1.get(),
    #     ent2.get(),
    #     ent3.get(),
    #     ent4.get())
    #     sqlCon.commit()
    #     sqlCon.close()
    #     messagebox.showinfo("Mysql Connection","Record Entered Successfully")


def delete_customer():
    customer_id = ent1.get()
    if messagebox.askyesno("Confirm Delete", "Are you sure to delete this customer?"):
        query = "DELETE FROM customers WHERE id = Customer ID"
        cursor.execute(query)
        clear()
    else:
        return True

mydb = mysql.connector.connect(host="localhost", user="user", passwd="user", database="cox", auth_plugin="mysql_native_password")
cursor = mydb.cursor()
root = Tk()



q=StringVar
t1=StringVar
t2=StringVar
t3=StringVar
t4=StringVar

wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height = "6")
trv.pack()

trv.heading(1, text="Customer ID")
trv.heading(2, text="First Name")
trv.heading(3, text="Last Name")
trv.heading(4, text="Age")

trv.bind('<Double 1>', getrow)

query = "SELECT ID, FIRST_NAME, LAST_NAME, AGE FROM CUSTOMERS"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#select table
lbl=Label(wrapper2, text="Search")
lbl.pack(side=tk.LEFT, padx=10)
ent=Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn=Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn=Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)



#User data section
lbl1=Label(wrapper3, text="Customer ID")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1=Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2=Label(wrapper3, text="First Name")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2=Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3=Label(wrapper3, text="Last Name")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3=Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4=Label(wrapper3, text="Age")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4=Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

up_btn=Button(wrapper3, text="Update", command=update_customer)
up_btn.grid(row=4, column=1, padx=5, pady=3)
add_btn=Button(wrapper3, text="Add new", command=add_new)
add_btn.grid(row=4, column=0, padx=5, pady=3)
del_btn=Button(wrapper3, text="Delete", command=delete_customer)
del_btn.grid(row=4, column=2, padx=5, pady=3)

root.title("My application")
root.geometry("800x700")
root.mainloop()