# from tkinter import *
# root=Tk()
# root.geometry("744x433")
# root.title("My GUI With Waqarul")
#
#
# """
# Important Label Options
# text-adds the text
# bd-background
# fg-foreground
# font-sets the font
# font=("comicsansms",19,"bold")
# padx-x padding
# pady-y padding
# relief- border styling -SUNKEN,RAISED,GROOVE,RIDGE
# """
# root=Label(text='''Abdul Rashid Salim Salman Khan (pronounced [səlˈmɑːn xɑːn]; born 27 \nDecember 1965\n)[3] is an Indian actor, film producer, writer and television personality who works predominantly in Hindi films. \nIn a film career spanning over thirty five years, Khan has received numerous awards, including \ntwo National Film Awards as a film producer, and two Filmfare Awards as an actor.[4]\n He is cited in the media as one of the most commercially successful actors\n of Indian cinema.[5][6] Forbes has included Khan in listings of the highest-paid celebrities in the \nworld, in 2015 and 2018, with him being the highest-ranked Indian in the latter year.
#
# ''',bg="red",fg="white",padx=113,pady=94,#method 1 using tuple font=("comicsansms",19,"bold") method 2 using string=
#  font="comicsansms 19 bold"
#            ,borderwidth=3,relief=SUNKEN
#            )
#
# # side=top,bottom,left,right
# # Important Pack Options
# # root.pack(anchor="nw")
# # root.pack(anchor="ne")
# # root.pack(side=BOTTOM ,anchor="se")
# # fill
# # padx
# pady
# root.pack(side=BOTTOM ,anchor="sw",fill=X)
# root.pack(side=LEFT,fill=Y,padx=34,pady=34)
# 16 4
#
# # root.pack()
# root.mainloop()

# Quick quiz:make 500x400 tkinter window and make a small strip in the botton and write ready in the center
import tkinter
root=tkinter.Tk()
root.geometry("500x400")
root.minsize(400,400)
root.title("Tkinter quick quiz 2")
root=tkinter.Label(text="Ready",fg="yellow",padx=100,pady=100,font="comicsansms 50 bold")
root.pack()
root1=tkinter.Label(text="",bg="grey",padx=1012,pady=40)
root1.pack(side=tkinter.BOTTOM ,anchor="sw",fill=tkinter.X)
root.mainloop()