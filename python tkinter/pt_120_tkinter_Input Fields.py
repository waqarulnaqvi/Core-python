# 23 2
# 24 17
from tkinter import *
# In tkinter everything is a widget
#fg means Foreground color for the widget.
# the people, objects, countryside, etc. in a picture or photograph
# that seem nearest to you and form its main part:
root=Tk()
e=Entry(root,width=50,bg="sky blue",fg="white",borderwidth=5)
e.pack()
e.get()#you get the values you typed it in the button
e.insert(0,"Enter Your Stock Quote ")#put default text inside of the text box
def myClick():
    myLabel=Label(root,text="Hello" +e.get())
    myLabel.pack()
myButton=Button(root,text="Click Me!!",bg="#000000",fg="Blue",padx=23,pady=34,command=myClick)
myButton.pack()

root.mainloop()