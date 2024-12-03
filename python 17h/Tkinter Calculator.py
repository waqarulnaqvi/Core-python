from tkinter import *
import time

def function(f1,str1,str2,str3,str4):
    # Frame 1 to 5
    f = Frame(f1, bg="grey")
    Nine = Button(f, text=str1, font="lucida 25 bold", fg="white", bg="green", padx=28, pady=22)
    Nine.pack(side=LEFT, padx=18, pady=12)
    Nine.bind("<Button-1>", click)

    Eight = Button(f, text=str2, font="lucida 25 bold", fg="white", bg="green", padx=28, pady=22)
    Eight.pack(side=LEFT, padx=18, pady=12)
    Eight.bind("<Button-1>", click)

    Seven = Button(f, text=str3, font="lucida 25 bold", fg="white", bg="green", padx=28, pady=22)
    Seven.pack(side=LEFT, padx=18, pady=12)
    Seven.bind("<Button-1>", click)

    Seven = Button(f, text=str4, font="lucida 25 bold", fg="white", bg="green", padx=28, pady=22)
    Seven.pack(side=LEFT, padx=18, pady=12)
    Seven.bind("<Button-1>", click)
    f.pack()
def click(event):
    global scvalue
    text=event.widget.cget("text") #cget function is used to get the text from the widget
    # print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())

        else:
            try:
              value=eval(screen.get())#eval is already told by cwh in his absolute beginner playlist.
            except Exception as e:
                value="Error"
                print(e)
                scvalue.set(value)
                screen.update()
                time.sleep(1)
                scvalue.set("")
                screen.update()
                return

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    elif text=="|X|":
        rem=""
        count=0
        for i in scvalue.get():
            count+=1
            if count!=len(scvalue.get()):
               rem+=i
        scvalue.set(rem)
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root=Tk()
root.geometry("644x800")
root.minsize(644,800)
root.title("Calculator by Mysterious Coder")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=Y,ipadx=10,ipady=10)

f1=Frame(root,bg="grey")
function(f1,"9","8","7","C")#Frame 1
function(f1,"6","5","4","+")#Frame 2
function(f1,"3","2","1","-")#Frame 3
function(f1,"C","0","=","*")#Frame 4
function(f1,"%",".","|X|","/")#Frame 5
f1.pack()
root.mainloop()
