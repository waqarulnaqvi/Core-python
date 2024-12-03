# 23 2
# 24 17
from tkinter import *
# In tkinter everything is a widget
root=Tk()
root.geometry("400x500")
# Tkinter is all about creating a thing and putting all the things on the screen.

# If nothing is in the column 2,3 in grid then tkinter ignored it and put column 4 value in column 2.
#Creating a Label Widget
myLabel0=Label(root,text="Hello world")
myLabel0.grid(row=0,column=0)
myLabel1=Label(root,text="")
myLabel1.grid(row=1,column=2)
myLabel2=Label(root,text="")
myLabel2.grid(row=1,column=3)
myLabel3=Label(root,text="My Name is Waqarul Naqvi")
myLabel3.grid(row=1,column=4)
myLabel3=Label(root,text="                       ")
myLabel3.grid(row=1,column=5)
myLabel4=Label(root,text="My Name is Waqarul Naqvi")
myLabel4.grid(row=1,column=6)

root.mainloop()
# Grid is little better than pack