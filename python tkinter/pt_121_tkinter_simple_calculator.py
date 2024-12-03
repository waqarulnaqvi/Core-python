from tkinter import *
root=Tk()
len=0
def button_click(number):
    current=e.get()
    e.delete(0,END)
    global len
    len+=1
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num= int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num= int(first_number)
    e.delete(0,END)

def button_substract():
    first_number=e.get()
    global f_num
    global math
    math="substraction"
    f_num= int(first_number)
    e.delete(0,END)
def button_divide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num= int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
       e.insert(0,f_num+int(second_number))
    elif math=="substraction":
        e.insert(0,f_num-int(second_number))
    elif math=="division":
        e.insert(0,f_num/int(second_number))
    elif math=="multiplication":
        e.insert(0,f_num*int(second_number))

def button_C():
    global len
    len-=1
    e.delete(len,END)


root.title("Simple Calculator")
root.geometry("415x655")
root.maxsize(415,655)
e=Entry(root,bg="light grey",width=65,borderwidth=5)
e.get()
# e.insert(0,"0")
e.grid(row=0,column=0,columnspan=3,ipady=20)
# columnspan used 3 column space so that we can put 3 buttons under the columnspan.

# Define buttons and put the buttons on the screen.
button_a = Button(root, text="1", padx=60, pady=30,bg="grey",fg="white" ,command=lambda :button_click(1))
button_b = Button(root, text="2", padx=60, pady=30,bg="grey",fg="white"  ,command=lambda: button_click(2))
button_c = Button(root, text="3", padx=60, pady=30,bg="grey",fg="white"  ,command=lambda: button_click(3))
button_a.grid(row=1,column=0)
button_b.grid(row=1,column=1)
button_c.grid(row=1,column=2)

button_d = Button(root, text="4", padx=60, pady=30,bg="grey",fg="white"  ,command=lambda: button_click(4))
button_e = Button(root, text="5", padx=60, pady=30,bg="grey",fg="white" ,command=lambda: button_click(5) )
button_f = Button(root, text="6", padx=60, pady=30,bg="grey",fg="white"  ,command=lambda: button_click(6))
button_d.grid(row=2,column=0)
button_e.grid(row=2,column=1)
button_f.grid(row=2,column=2)

button_g = Button(root, text="7", padx=60, pady=30,bg="grey",fg="white" ,command=lambda: button_click(7) )
button_h = Button(root, text="8", padx=60, pady=30,bg="grey",fg="white" ,command=lambda: button_click(8) )
button_i = Button(root, text="9", padx=60, pady=30,bg="grey",fg="white" ,command=lambda: button_click(9) )
button_g.grid(row=3,column=0)
button_h.grid(row=3,column=1)
button_i.grid(row=3,column=2)

button_j = Button(root, text="(", padx=60, pady=30,bg="blue",fg="white"  ,command=lambda: button_click("("))
button_k = Button(root, text="0", padx=60, pady=30,bg="grey",fg="white"  ,command=lambda: button_click("0"))
button_l = Button(root, text=")", padx=60, pady=30,bg="blue",fg="white" ,command=lambda: button_click(")") )
button_j.grid(row=4,column=0)
button_k.grid(row=4,column=1)
button_l.grid(row=4,column=2)

button_plus = Button(root, text="+", padx=60, pady=30,bg="sky blue" ,command=button_add)
button_minus = Button(root, text="-", padx=60, pady=30,bg="sky blue" ,command=button_substract )
button_multiply = Button(root, text="*", padx=60, pady=30,bg="sky blue" ,command= button_multiply )
button_plus.grid(row=5,column=0)
button_minus.grid(row=5,column=1)
button_multiply.grid(row=5,column=2)

button_clear = Button(root, text="clear", padx=120, pady=30,bg="red",fg="white" ,command=button_clear)
buttondivide = Button(root, text="/", padx=60, pady=30,bg="sky blue",command=lambda: button_divide)
button_clear.grid(row=6,column=0,columnspan=2)
buttondivide.grid(row=6,column=2)

button_clr = Button(root, text="C", padx=60, pady=30,bg="red",fg="white" ,command=button_C)
button_equal = Button(root, text="=", padx=130, pady=30,bg="green",fg="white",command=button_equal)
button_clr.grid(row=7,column=0)
button_equal.grid(row=7,column=1,columnspan=2)

root.config(bg="black")
root.mainloop()

# 22 24
# 23 54