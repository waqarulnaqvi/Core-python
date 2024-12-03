from tkinter import *
def myfunc():
    print("I am evil function")

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
root.config(menu=filemenu)
root.mainloop()