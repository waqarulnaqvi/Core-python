# 16 28
from tkinter import *
def food():
    print(f"Name is {namevalue.get()}")
    print(f"phone number is {phonevalue.get()}")
    print(f"Gender is {gendervalue.get()}")
    print(f"Emergency number is {emergencyvalue.get()}")
    print(f"Payment mode is {pmodevalue.get()}")
    print(f"food service is {foodservicevalue.get()}")
    print("Value is submitted!!\n")#quick quiz 5
root=Tk()
root.geometry("644x344")
root.title("Grid layout")
Label(root,text="Welcome to Waqarul Travels",bg="red",fg="white",font="comicsansms 13 bold").grid(row=0,column=3)
name=Label(root,text="Name").grid(row=1,column=2)
phone=Label(root,text="Phone").grid(row=2,column=2)
gender=Label(root,text="Gender").grid(row=3,column=2)
e_contact=Label(root,text="Emergency Contact").grid(row=4,column=2)
p_mode=Label(root,text="Payment Mode").grid(row=5,column=2)

namevalue=StringVar()
phonevalue=IntVar()
gendervalue=StringVar()
emergencyvalue=IntVar()
pmodevalue=StringVar()
foodservicevalue=IntVar()#checkbox

#packing the entries

nameentry=Entry(root,textvariable=namevalue).grid(row=1,column=3)
phoneentry=Entry(root,textvariable=phonevalue).grid(row=2,column=3)
genderentry=Entry(root,textvariable=gendervalue).grid(row=3,column=3)
emergencyentry=Entry(root,textvariable=emergencyvalue).grid(row=4,column=3)
pmodeentry=Entry(root,textvariable=pmodevalue).grid(row=5,column=3)

# checkbox
foodservice=Checkbutton(text="Want to prebook your meals",variable=foodservicevalue).grid(row=6,column=3)
Button(text="Submit now",command=food,fg="white",bg="green").grid(row=7,column=3)
root.mainloop()

# 17 9