from tkinter import *
root=Tk()
root.geometry("455x233")
root.title("Scrollbar tutorial")
# For connecting scrollbar to a widget
# 1.widget(yscrollcommand =scrollbar.set)
# 2.scrollbar.config(command=widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item {i}")

# Quick quiz 9:
text='''# from tkinter import *\n
# # root=Tk()\n
# # root.geometry("455x233")\n
# # root.title("Scrollbar tutorial")\n
# # # For connecting scrollbar to a widget\n
# # # 1.widget(yscrollcommand =scrollbar.set)\n
# # # 2.scrollbar.config(command=widget.yview)\n
# # scrollbar=Scrollbar(root)\n
# # scrollbar.pack(side=RIGHT,fill=Y)\n
# # listbox=Listbox(root,yscrollcommand=scrollbar.set)\n
# # for i in range(344):\n
# #     listbox.insert(END,f"Item {i}")\n
# #\n
# # # listbox.pack(fill="both",padx=22,pady=22)\n
# # text=Text(root,yscrollcommand=scrollbar.set)\n
# # text.pack(fill=BOTH)\n
# #\n
# scrollbar.config(command=text.yview)\n
# # # scrollbar.config(command=listbox.yview)\n
# #\n
# # root.mainloop()\n
# # exit()\n'''
sum=""
for i in text:
    sum+=i
    if(i=="\n"):
      listbox.insert(END,sum)
      sum=""
listbox.pack(fill="both",padx=22,pady=22)
# text=Text(root,yscrollcommand=scrollbar.set)
# text.pack(fill=BOTH)

# scrollbar.config(command=text.yview)
scrollbar.config(command=listbox.yview)

root.mainloop()
# # exit()








# # # Quick Quiz 9:
# # Connect scrollbar with big label
# from tkinter import *
# root=Tk()
# root.geometry("455x233")
# root.title("Quick quiz 9")
# scrbar=Scrollbar(root)
# scrbar.pack(side=RIGHT,fill=Y)
# lbl=Label(text="Quick Quiz 9",bg="sky blue",fg="white",font="lucida 33 bold")
# lbl1=Label(text="""# from tkinter import *
# # root=Tk()
# # root.geometry("455x233")
# # root.title("Scrollbar tutorial")
# # # For connecting scrollbar to a widget
# # # 1.widget(yscrollcommand =scrollbar.set)
# # # 2.scrollbar.config(command=widget.yview)
# # scrollbar=Scrollbar(root)
# # scrollbar.pack(side=RIGHT,fill=Y)
# # listbox=Listbox(root,yscrollcommand=scrollbar.set)
# # for i in range(344):
# #     listbox.insert(END,f"Item {i}")
# #
# # # listbox.pack(fill="both",padx=22,pady=22)
# # text=Text(root,yscrollcommand=scrollbar.set)
# # text.pack(fill=BOTH)
# #
# scrollbar.config(command=text.yview)
# # # scrollbar.config(command=listbox.yview)
# #
# # root.mainloop()
# # exit()""",font="lucida 10 bold")
# lbl.pack()
# lbl1.pack()
# # list_frame=Frame(root)
# # list_frame.pack()
#
#
# # scrbar.config()
# root.mainloop()

# 15 10