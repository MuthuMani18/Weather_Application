from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox
import tkinter.messagebox
kal=Tk()
res=StringVar()
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="muthu")
abc=mydb.cursor()
def add():
    rollno=e1.get()
    name=e2.get()
    course=e3.get()
    abc.execute("insert into stu values('"+rollno+"','"+name+"','"+course+"')")
    mydb.commit()
    messagebox.showinfo("success","datta inserted")
def sub():
    rollno=e1.get()
    name=e2.get()
    course=e3.get()
    abc.execute("update stu set name='"+name+"',course='"+course+"' where rollno='"+rollno+"'")
    mydb.commit()
    messagebox.showinfo("success","data updated")

def mul():
    rollno = e1.get()

    abc.execute("delete  from stu where rollno='" + rollno + "'")
    mydb.commit()
    messagebox.showinfo("success","data deleted")

l1=Label(kal,text="RollNo=").grid(row=0,column=0)
l2=Label(kal,text="Name=").grid(row=1,column=0)
l3=Label(kal,text="Course=").grid(row=2,column=0)

e1=Entry(kal)
e2=Entry(kal)
e3=Entry(kal,textvariable=res)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

b1=Button(kal,text="INSERT",command=add).grid(row=0,column=2)
b2=Button(kal,text="UPDATE",command=sub).grid(row=1,column=2)
b3=Button(kal,text="DELETE",command=mul).grid(row=2,column=2)
'''
def sayhi():
    print("hi da")

txt=StringVar()
#label
Name=Label(kal,text="Name",fg="blue",bg="yellow",font=("calibri",14)).pack()
#entry
e1=Entry(kal,textvariable=txt).pack()
txt.set("im kaleesh")

#button
b1=Button(kal,text="click",command=sayhi).pack()
'''
kal.mainloop()

#Grid
