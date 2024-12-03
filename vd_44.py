from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global  file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*,txt")])
    if file=="":
        file=None
    else:
        try:
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()
        except Exception as e:
            print(e)

def saveFile():
    global file
    if file ==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*,txt")])
        if file =="":
            file=None
        else:
#           #save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            # print("File Saved")
    else:
        #save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def cut():
    TextArea.event_generate("<<Cut>>")#It will automatically handled cut event.
def copy():
    TextArea.event_generate("<<Copy>>")#It will automatically handled cut event.
def paste():
    TextArea.event_generate("<<Paste>>")#It will automatically handled cut event.
def about():
    tkinter.messagebox.showinfo("Notepad","Notepad by waqarul naqvi")


if __name__=='__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("11.png")
    root.geometry("644x788")

    # Add TextArea
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    # Lets create a menubar
    MenuBar=Menu(root)

    # File Menu Start
    fileMenu=Menu(MenuBar,tearoff=0)
    # To open new file
    fileMenu.add_command(label="New",command=newFile)

    # To open already existing file
    fileMenu.add_command(label="Open",command=openFile)

    # To save the current file
    fileMenu.add_command(label="Save",command=saveFile)
    fileMenu.add_separator()

    fileMenu.add_command(label="Exit",command=root.destroy)
    # File Menu Ends
    MenuBar.add_cascade(label="File",menu=fileMenu)

    # Edit Menu Starts
    Editmenu=Menu(MenuBar,tearoff=0)
    # To give a feature of cut,copy and paste
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)
    # Edit Menu Ends
    MenuBar.add_cascade(label="Edit",menu=Editmenu)

    # Help Menu Starts
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    # Help Menu Ends
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    root.config(menu=MenuBar)

    # Adding Scrollbar
    scrollbar=Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
