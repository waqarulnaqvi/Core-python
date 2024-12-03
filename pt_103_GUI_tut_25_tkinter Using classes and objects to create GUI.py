# from tkinter import *
# import tkinter.messagebox
#
# class GUI(Tk):
#     def __init__(self):
#         # root=self=window
#         super().__init__()
#         self.geometry("744x377")
#
#     def status(self):
#         self.var=StringVar()
#         self.var.set("Ready")
#         self.statusbar=Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
#         self.statusbar.pack(side=BOTTOM,fill=X)
#
#     def createbutton(self,inptext):
#         Button(text=inptext,command=self.click).pack()
#
#     def click(self):
#         tkinter.messagebox.showinfo("Support","Button clicked!!")
#
# if __name__ =='__main__':
#     window=GUI()
#     window.status()
#     window.createbutton("Click me")
#     window.mainloop()

#Quick quiz 10: create a class and tell what the class will do.

from tkinter import *
import tkinter.messagebox
# This Gui create a menus and submenus and call the functin click

class Menu_and_submenu(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")

    def mainMenu(self):
        self.main_menu = Menu(self)
        self.main_menu.add_cascade(label=input("Enter file menu 1 :"),menu=self.subMenu())
        self.main_menu.add_cascade(label=input("Enter file menu 2 :"),menu=self.subMenu())
        self.config(menu=self.main_menu)

    def click(self):
        tkinter.messagebox.showinfo("Support","Button clicked!!")
    def subMenu(self):
        self.smenu = Menu(self.main_menu, tearoff=0)
        for i in range(int(input("Enter total submenu :"))):
            self.smenu.add_command(label=input(f"Enter value {i+1} :"), command=self.click)
        return self.smenu

if __name__=="__main__":
    window=Menu_and_submenu()
    window.mainMenu()
    window.mainloop()

exit()

# filemenu=Menu(root)
# m1=Menu(filemenu,tearoff=0)#menu me jo patli se dot dot karke line aa rhi wo gayab ho jaayegi
# m1.add_command(label="Open project",command=myfunc)
# m1.add_command(label="New project",command=myfunc)
# m1.add_separator()#it will add separator in the project
# m1.add_command(label="Save",command=myfunc)
# m1.add_command(label="Save as",command=myfunc)
# m1.add_command(label="Print",command=myfunc)
# root.config(menu=filemenu)
# # root.config(menu=m1)
# filemenu.add_cascade(label="File",menu=m1)
#
# m2=Menu(filemenu,tearoff=0)#menu me jo patli se dot dot karke line aa rhi wo gayab ho jaayegi
# m2.add_command(label="view",command=myfunc)
# m2.add_command(label="view as",command=myfunc)
# m2.add_separator()#it will add separator in the project
# m2.add_command(label="cut",command=myfunc)
# m2.add_command(label="copy",command=myfunc)
# m2.add_command(label="paste",command=myfunc)
# m2.add_command(label="undo",command=myfunc)
# filemenu.add_cascade(label="Edit",menu=m2)
# root.config(menu=filemenu)
# root.mainloop()