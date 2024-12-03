from tkinter import *
from PIL import ImageTk,Image
# from PIL import ImageTk,Image

def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text

root=Tk()
root.title("Godi Media news")
root.geometry("800x2000")
root.maxsize(800,2000)

texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))
    image= Image.open(f"{i+1}.png")
    image=image.resize((225,265))
    # image=image.resize((225,265),Image.ANTIALIAS)
    #TODO: Resize these images
    photos.append(ImageTk.PhotoImage(image))

f0=Frame(root,width=800,height=70)
Label(f0,text="Godi Media News",font="lucida 33 bold").pack()
Label(f0,text="January 19 2050",font="lucida 13 bold").pack()
f0.pack()

heading=["Virat Kohli","Indian Eagle","Indian Supreme court"]

# Method 1:
for i in range(3):

    f1 = Frame(root, width=900, height=200,padx=22,pady=14)

    if (i == 1):
        Label(f1, image=photos[i], anchor="e").pack(side="right")
        f1.pack(anchor="w")
    else:
        Label(f1, image=photos[i], anchor="e").pack(side=LEFT)
        f1.pack(anchor="w")

    Label(f1,text=heading[i],font="lucida 20 bold",padx=12,pady=12).pack()

    Label(f1, text=texts[i], padx=22, pady=22).pack(side=LEFT)

# Method :2

# f1=Frame(root,width=900,height=200)
# Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
# Label(f1,image=photos[0],anchor="e").pack(side=LEFT)
# f1.pack(anchor="w")
#
#
# f1=Frame(root,width=900,height=200)
# Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
# Label(f1,image=photos[0],anchor="e").pack(side=LEFT)
# f1.pack(anchor="w")
#
#
# f1=Frame(root,width=900,height=200)
# Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
# Label(f1,image=photos[0],anchor="e").pack(side=LEFT)
# f1.pack(anchor="w")



root.mainloop()