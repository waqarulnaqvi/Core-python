from tkinter import *
from PIL import Image, ImageTk

base = Tk()
base.title("Yuniek's Newspaper")
base.geometry("1180x644")
base.minsize(width=300, height=300)

# Header for newspapaer
Header = Frame(base, bg="grey", borderwidth=5, relief=SUNKEN)
Header.pack(side=TOP, fill=X)
t = Label(Header, text="Yuniek's Newspaper", bg="grey", font="Arial 19 bold italic")
t.pack()

# News 1
f1 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f1.pack(fill=X, anchor='nw')

p1 = Image.open("1.png")
P1 = ImageTk.PhotoImage(p1)

l1 = Label(f1, image=P1, width=130, height=130)
l1.pack(side=LEFT)
l12 = Label(f1, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l12.pack()

# News 2
f2 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f2.pack(fill=X, anchor='nw')

p2 = Image.open("1.png")
P2 = ImageTk.PhotoImage(p2)

l2 = Label(f2, image=P2, width=130, height=130)
l2.pack(side=LEFT)
l22 = Label(f2, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l22.pack()

# News 3
f3 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f3.pack(fill=X, anchor='nw')

p3 = Image.open("1.png")
P3 = ImageTk.PhotoImage(p3)

l3 = Label(f3, image=P3, width=130, height=130)
l3.pack(side=LEFT)
l32 = Label(f3, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l32.pack()

# News 4
f4 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f4.pack(fill=X, anchor='nw')

p4 = Image.open("1.png")
P4 = ImageTk.PhotoImage(p4)

l4 = Label(f4, image=P4, width=130, height=130)
l4.pack(side=LEFT)
l42 = Label(f4, text='''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.''', bg="lightblue",)
l42.pack()
base.mainloop()

# Mylogic
# import tkinter
# from PIL import Image,ImageTk
# # (PIL =Python Imaging Library)
# root=tkinter.Tk()
# root.title("Godi Media")
# Header = tkinter.Frame(root, bg="grey", borderwidth=5, relief=tkinter.SUNKEN)
# Header.pack(side=tkinter.TOP, fill=tkinter.X)
# t = tkinter.Label(Header, text="GODI MEDIA", bg="grey", font="Arial 19 bold italic")
# t.pack()
#
# # NEWS 1
# NEWS1=tkinter.Frame(root, bg="lightblue", borderwidth="3", relief=tkinter.SUNKEN, highlightbackground="black", highlightthickness=1.5)
# NEWS1.pack(side=tkinter.TOP, fill=tkinter.X)
# t=tkinter.Label(NEWS1,text="Indian godi news", bg="Lightblue", font="Arial 19 bold italic")
# t.pack()
#
# p1 = Image.open("1.png")
# P1 = ImageTk.PhotoImage(p1)
# l1 = tkinter.Label(NEWS1, image=P1, width=644, height=200)
#
# news1=tkinter.Label(NEWS1,text='''New Delhi: The Supreme Court has denied an octogenarian man the right to divorce his wife of six decades, 27 years after he first applied to dissolve their marriage.
# Divorce remains taboo across much of India with only one in every 100 marriages ending in dissolution, often owing to family and social pressure to sustain unhappy marriages.
# Those seeking divorce must get approval from the courts, which typically only grant it if proof of cruelty, violence or undue financial demands is presented.
# That year his wife Paramjit Kaur Panesar, now 82, had refused to move with him to Chennai when the Indian Air Force posted him there.''',padx=113,pady=94,
#  font="comicsansms 5 bold"
#            ,borderwidth=3,relief=tkinter.SUNKEN)
# news1.pack(side=tkinter.RIGHT)
# l1.pack(side=tkinter.LEFT)
#
# # NEWS 2
# NEWS1=tkinter.Frame(root, bg="lightblue", borderwidth="3", relief=tkinter.SUNKEN, highlightbackground="black", highlightthickness=1.5)
# NEWS1.pack(side=tkinter.TOP, fill=tkinter.X)
# t=tkinter.Label(NEWS1,text="Indian godi news", bg="Lightblue", font="Arial 19 bold italic")
# t.pack()
#
# p1 = Image.open("1.png")
# P1 = ImageTk.PhotoImage(p1)
# l1 = tkinter.Label(NEWS1, image=P1, width=644, height=200)
#
# news1=tkinter.Label(NEWS1,text='''New Delhi: The Supreme Court has denied an octogenarian man the right to divorce his wife of six decades, 27 years after he first applied to dissolve their marriage.
# Divorce remains taboo across much of India with only one in every 100 marriages ending in dissolution, often owing to family and social pressure to sustain unhappy marriages.
# Those seeking divorce must get approval from the courts, which typically only grant it if proof of cruelty, violence or undue financial demands is presented.
# That year his wife Paramjit Kaur Panesar, now 82, had refused to move with him to Chennai when the Indian Air Force posted him there.''',padx=113,pady=94,
#  font="comicsansms 5 bold"
#            ,borderwidth=3,relief=tkinter.SUNKEN)
# news1.pack(side=tkinter.RIGHT)
# l1.pack(side=tkinter.LEFT)
#
# # NEWS 3
# NEWS1=tkinter.Frame(root, bg="lightblue", borderwidth="3", relief=tkinter.SUNKEN, highlightbackground="black", highlightthickness=1.5)
# NEWS1.pack(side=tkinter.TOP, fill=tkinter.X)
# t=tkinter.Label(NEWS1,text="Indian godi news", bg="Lightblue", font="Arial 19 bold italic")
# t.pack()
#
# p1 = Image.open("1.png")
# P1 = ImageTk.PhotoImage(p1)
# l1 = tkinter.Label(NEWS1, image=P1, width=644, height=200)
#
# news1=tkinter.Label(NEWS1,text='''New Delhi: The Supreme Court has denied an octogenarian man the right to divorce his wife of six decades, 27 years after he first applied to dissolve their marriage.
# Divorce remains taboo across much of India with only one in every 100 marriages ending in dissolution, often owing to family and social pressure to sustain unhappy marriages.
# Those seeking divorce must get approval from the courts, which typically only grant it if proof of cruelty, violence or undue financial demands is presented.
# That year his wife Paramjit Kaur Panesar, now 82, had refused to move with him to Chennai when the Indian Air Force posted him there.''',padx=113,pady=94,
#  font="comicsansms 5 bold"
#            ,borderwidth=3,relief=tkinter.SUNKEN)
# news1.pack(side=tkinter.RIGHT)
# l1.pack(side=tkinter.LEFT)
# root.geometry("1180x644")
# root.mainloop()
#  # 18 30