# from tkinter import *
#
# root=Tk()
# root.geometry("655x333")
# def hello():
#     print("Hello tkinter Buttons")
# def name():
#     print("Waqarul\n")
# f1=Frame(root,borderwidth=6,bg="white",relief=SUNKEN)
# f1.pack(side=LEFT,anchor="nw")
# # anchor nw is dene se yeah hoga ki yeah upper label jaayega
# b1=Button(f1,fg="red",text="Print now",command=hello)
# b1.pack(side=LEFT)
#
# b2=Button(f1,fg="red",text="Tell me your name",command=name)
# b2.pack(side=LEFT,padx=28)
#
# b3=Button(f1,fg="red",text="Print now")
# b3.pack(side=LEFT,padx=28)
#
# b4=Button(f1,fg="red",text="Print now")
# b4.pack(side=LEFT,padx=28)
# root.mainloop()
#
#Quick quiz 3
def hello():
    print("Hello tkinter Buttons")
def name():
    print("Waqarul\n")
from  tkinter import *
root=Tk()
root.geometry("655x333")
f1=Frame(root,bg="skyblue",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1,fg="red",text="Enter",command=name)
b1.pack(side=LEFT,padx=30)

b1=Button(f1,fg="red",text="Enter",command=name)
b1.pack(side=LEFT,padx=30)

b1=Button(f1,fg="red",text="Enter",command=hello)
b1.pack(side=LEFT,padx=30)

b1=Button(f1,fg="red",text="Enter",command=name)
b1.pack(side=LEFT,padx=30)

root.mainloop()
