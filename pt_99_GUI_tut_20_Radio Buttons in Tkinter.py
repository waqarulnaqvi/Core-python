import tkinter.messagebox
from tkinter import *
def order():
    tkinter.messagebox.showinfo("Order",f"{var.get()} order has been successful!")
root=Tk()
root.geometry("644x344")
root.title("Radio Buttons in Tkinter")

# var =IntVar()
var =StringVar()
var.set("No")#if you don't give intitial value to the variable then all values would be selected!!
# var.set(1)
Label(root,text="What would you like to have sir?",justify=LEFT,font="lucida 19 bold",padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value="samosa").pack(anchor="w")

Button(text="order now",bg="green",fg="white",command=order).pack()
root.mainloop()