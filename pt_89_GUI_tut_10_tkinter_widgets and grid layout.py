# from tkinter import *
#
# def getvals():
#     print(f"The value of username is {uservalue.get()}")
#     print(f"The value of password is {passvalue.get()}")
# root=Tk()
# root.geometry("644x344")
# root.title("Tut 10 tkinter")
#
# # GRID layout:
#
# a=Label(root,text="username")
# password=Label(root,text="password")
#
# # another method to pack the value
# # a.grid(row=0 by default,column=0 by default)
# # password.grid(row =0 by default,column =0 by default)
#
# a.grid()
# password.grid()
#
#
# # Entry widget is used to take input from the user.
# # Variable classes in tkinter
# # BooleanVar, DoubleVar, IntVar, StringVar
#
# uservalue=StringVar()
# passvalue=StringVar()
#
# userentry=Entry(root,textvariable=uservalue)
# passentry=Entry(root,textvariable=passvalue)
#
# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)
#
# Button(text="Submit",command=getvals).grid()
# root.mainloop()

# Quick quiz 4: wap to make dance class form and stores all the value in the file.
from tkinter import *
def submitnow():
    print(f"Name is : {name1.get()}")
    print(f"Password is : {pass1.get()}\n")
    with open("pt_89_GUI_tut_10_tkinter_dance.txt","a") as f:
        f.writelines(f"Name is : {name1.get()}\nPassword is : {pass1.get()}\n\n")

root=Tk()
root.title("Dance class entry form")
root.geometry("644x344")
f1=Frame(borderwidth=4,relief=SUNKEN,bg="yellow").grid(row=12,column=12)
t = Label(f1, text="Dance class", bg="grey", font="Arial 19 bold italic").grid(row=0,column=20)
name=Label(f1,text="Name :",fg="red").grid(row=1,column=1)
password=Label(f1,text="Password :",fg="red").grid(row=4,column=1)


name1=StringVar()
pass1=StringVar()
nameentry=Entry(f1,textvariable=name1).grid(row=1,column=2)
passentry=Entry(f1,textvariable=pass1).grid(row=4,column=2)
Button(text="Submit now",bg="green",fg="white",command=submitnow).grid(row=5,column=2)

root.mainloop()