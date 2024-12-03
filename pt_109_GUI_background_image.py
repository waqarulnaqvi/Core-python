from tkvideo import tkvideo
from tkinter import *
from PIL import Image,ImageTk

def stoping():
    return exit()
root=Tk()
root.geometry("960x750")
root.maxsize(960,750)

# Load the background image
image=Image.open('jarvis__bg.jpg')
image=image.resize((960,750))
photo=ImageTk.PhotoImage(image)

# Create a Label Widget to display the background image
bl=Label(root,image=photo)
bl.place(x=0,y=0,relwidth=1,relheight=1)
f1=Frame(root,bg="grey")
f1.pack()
lblvideo = Label(f1)
lblvideo.pack()
lblvideo1 = Label(root)
lblvideo1.pack()
tkvideo("jarvis_background.mp4", lblvideo, loop=1, size=(200, 130)).play()
tkvideo("heading.gif",lblvideo,loop=1,size=(200,130)).play()
Button(f1,text="Stop jarvis",fg="white",bg="red",relief=SUNKEN,borderwidth=6,command=stoping).pack()
Label(text="Good Morning!!",relief=SUNKEN,borderwidth=4,font="lucida 12 italic",fg="white",bg="green").pack(anchor="nw")
Label(text="I am Jarvis AI,Please tell me how may I help you",relief=SUNKEN,borderwidth=4,font="lucida 12 italic",fg="white",bg="green").pack(anchor="nw")
Label(text="Listening..",relief=SUNKEN,borderwidth=4,font="lucida 12 italic",fg="white",bg="blue").pack(anchor="nw")
Label(text="Recognizing..",relief=SUNKEN,borderwidth=4,font="lucida 12 italic",fg="white",bg="blue").pack(anchor="nw")
# tkvideo("jarvislistening.gif",lblvideo1,loop=1,size=(80,100)).play()



# bgi=PhotoImage(file="jarvis_background.mp4")
#
# bl=Label(root,image=bgi)
# bl.place(relwidth=1,relheight=1)

# bgimg = PhotoImage(file="jarvisbackground.webp")
# img=ImageTk.PhotoImage(Image.open('2.png'))
# lbl=Label(image=img,width=850,height=755)
root.mainloop()

# 22 46
# 00 6