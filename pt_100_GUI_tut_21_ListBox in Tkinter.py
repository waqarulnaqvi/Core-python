from tkinter import *
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

root=Tk()
i=0
root.geometry("544x444")
root.title("Listbox tutorial")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")
Button(root,text="Add Item",command=add).pack()
root.mainloop()