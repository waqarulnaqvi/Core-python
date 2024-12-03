from tkinter import *
root=Tk()
root.geometry("655x444")
root.title("CodeWithHarry - Title of My GUI")
root.wm_iconbitmap("11.png")
root.configure(background="grey")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")# Monitor width and height
Button(text="Close",command=root.destroy).pack()
root.mainloop()



# 16 52