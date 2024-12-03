from tkinter import *
import tkinter.messagebox as tmsg
def divya():
    ans=tmsg.askretrycancel("Divya se dosti kar lo","sorry divya nahi banegi aapki dost")
    if ans:
        tmsg.showinfo("Divya","Retry karne pe bhi kuch nahi hoga!")
    else:
        tmsg.showinfo("Divya","Good decision!")

def myfunc():
    print("I am evil function")
def help():
    print("I will help you!!")
    a=tmsg.showinfo("Help","Waqarul will help you with this gui")
    # print(a) #return value is ok

def rate():
    print("Rate us")
    value=tmsg.askquestion("Was your experience good?","You used this gui..Was your experience good?")
    if value=="yes":
        msg="Great. Rate us on appstore please"
    else:
        msg="Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience",msg)

    # print(value)
root=Tk()
root.geometry(f"500x400")
root.title("menus and submenus")

# Use these to create a non-drop down menu:
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Quit",command=quit)
# root.config(menu=mymenu)

filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)#menu me jo patli se dot dot karke line aa rhi wo gayab ho jaayegi
m1.add_command(label="Open project",command=myfunc)
m1.add_command(label="New project",command=myfunc)
m1.add_separator()#it will add separator in the project
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=filemenu)
# root.config(menu=m1)
filemenu.add_cascade(label="File",menu=m1)

m2=Menu(filemenu,tearoff=0)#menu me jo patli se dot dot karke line aa rhi wo gayab ho jaayegi
m2.add_command(label="view",command=myfunc)
m2.add_command(label="view as",command=myfunc)
m2.add_separator()#it will add separator in the project
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="undo",command=myfunc)
filemenu.add_cascade(label="Edit",menu=m2)


m3=Menu(filemenu,tearoff=0)#menu me jo patli se dot dot karke line aa rhi wo gayab ho jaayegi
m3.add_command(label="Help",command=help)
m3.add_command(label="Support",command=help)
m3.add_command(label="Be friend Divya",command=divya)
m3.add_command(label="Rate us",command=rate)
filemenu.add_cascade(label="Help",menu=m3)
root.config(menu=filemenu)

root.mainloop()
# 17 19