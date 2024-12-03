# from tkinter import *
# root=Tk()
#
# def Deepak():
#     root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")
#
# root.minsize(400,175)
# root.title("Program to exchange the size of GUI")
#
# Label(root,text="DEEPAK GUI EXCHANGE",font="comicsansms 13 bold",pady=20,padx=30,fg="green").grid(row=0,column=2)
#
# width=Label(root,text="Enter GUI weidth number above 400  :-",fg="blue")
# height=Label(root,text="Enter GUI height number above 175  :-",fg="blue")
#
# width.grid(row=1,column=2)
# height.grid(row=2,column=2)
#
# widthvalue=StringVar()
# heightvalue=StringVar()
#
# widthentry=Entry(root,textvariable=widthvalue,bg="Powder blue")
# heightentry=Entry(root,textvariable=heightvalue,bg="Powder blue")
# widthentry.grid(row=1,column=3)
# heightentry.grid(row=2,column=3)
#
# Button(root,text="Plese Submit",command=Deepak,pady=10,bg="Powder blue").grid(row=3,column=3)
#
# root.mainloop()
# exit()
"""Create a gui window which takes as input width and height and upon clicking apply, it should be able to change its size accordingly"""
from tkinter import *


root=Tk()
root.geometry("300x200")
def resizesize():
    width = widthvalue.get()
    height = heightvalue.get()
    root.geometry(f"{width}x{height}")
Label(text="Image Resizer",bg="red",fg="white",font="BalluBhai 20 italic").grid(row=0,column=4)
Label(text="Width" ,fg="red",anchor="ne",pady=3,padx=3).grid()
Label(text="Height" ,fg="red",anchor="ne",pady=3,padx=3).grid()
pmodevalue=StringVar()
foodservicevalue=IntVar()#checkbox

#packing the entries
widthvalue=StringVar()
heightvalue=StringVar()

widthentry=Entry(root,textvariable=widthvalue).grid(row=1,column=4)
heightentry=Entry(root,textvariable=heightvalue).grid(row=2,column=4)

Button(text="Resize",bg="green",fg="white",command=resizesize).grid(row=3,column=4)
# f1.pack()
root.mainloop()

# 15 23