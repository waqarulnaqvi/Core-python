from tkinter import  *
root=Tk()
root.title("tkinter tutorial 8")
root.geometry("655x333")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y",pady="121")

f2=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Project Tkinter - Pycharm",font="Helvetica 16 italic")
l.pack(pady=150)

l=Label(f2,text="Welcome to subline text",font="BalluBhai 16 bold",fg="red",pady="30")
l.pack()

root.mainloop()