# 23 2
# 24 17
from tkinter import *
# In tkinter everything is a widget
#fg means Foreground color for the widget.
# the people, objects, countryside, etc. in a picture or photograph
# that seem nearest to you and form its main part:
root=Tk()
def myClick():
    myLabel=Label(root,text="Look! I clicked a Button!!")
    myLabel.pack()
# root.geometry("400x500")
# Tkinter is all about creating a thing and putting all the things on the screen.

# myButton=Button(root,text="Click Me!!",state=DISABLED,padx=23,pady=34,command=myClick)
# myButton.pack()
myButton=Button(root,text="Click Me!!",bg="#000000",fg="Blue",padx=23,pady=34,command=myClick)
myButton.pack()

root.mainloop()