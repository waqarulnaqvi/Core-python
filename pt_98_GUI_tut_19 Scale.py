# import tkinter.messagebox
# from tkinter import *
# def getdollar():
#     print(f"we have credited {myslider2.get()} dollars to your bank account")
#     tkinter.messagebox.showinfo("Bank account :",f"You have credited {myslider2.get()} dollars to your bank account")
# root=Tk()
# root.geometry("455x233")
# root.title("Slider tutorial")
# #
# # myslider=Scale(root,from_=0,to=100)
# # myslider.pack()
#
# Label(root,text="How many dollars do you want?").pack()
# myslider2=Scale(root,from_=10,to=100,orient=HORIZONTAL,tickinterval=20)
# myslider2.set(30)
# myslider2.pack()
# Button(root,text="Get dollars!",command=getdollar).pack()
# # myslider2.pack() //jidhar pack karoge button ko udhar button show hoga.
# root.mainloop()

# # exit()
#
# Quick quiz 8
# Ask user 0 to 10 rating of the food and store value in the file
import tkinter.messagebox
from tkinter import *
def thanks():
    tkinter.messagebox.showinfo("Support",f"Thanks for rating us!! {myslider.get()}")
    print("Support",f"Thanks for rating us!! {myslider.get()}")
    with open("pt_98_GUI.txt", "a") as f:
        f.writelines(f"Rating : {myslider.get()}\n\n")
def rate():
    value=tkinter.messagebox.askquestion("Was your experience good?","You used this gui..Was your experience good?")
    if value=="yes":
        Label(root,text="Rating",font="balluBhai 20 bold").pack()
        # myslider.set(10)
        myslider.pack()
        Button(root, text="Submit Rating", fg="white", bg="green", font="lucida 7 bold", command=thanks).pack()
    else:
        tkinter.messagebox.showinfo("Support","Our team work hard to improve your experience!!")



root=Tk()
root.geometry("455x355")
root.title("Quick quiz 8")

# Slider
myslider = Scale(root, from_=0, to=10, orient=HORIZONTAL)

# menu1
mnu=Menu(tearoff=0)
mnu.add_command(label="file")
mnu.add_command(label="view")

# menu2
m2=Menu(mnu,tearoff=0)
m2.add_command(label="help")
m2.add_command(label="support")
m2.add_command(label="rate us",command=rate)
mnu.add_cascade(label="help",menu=m2)
root.config(menu=mnu)
root.mainloop()