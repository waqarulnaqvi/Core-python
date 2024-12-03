
# 12 53
from tkinter import *
from tkvideo import tkvideo
from PIL import Image,ImageTk

class GUI_AI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x750")
        self.maxsize(960, 750)
        self.wm_iconbitmap("11.png")
        self.title("Jarvis A.I")
       # Load the background image
        image = Image.open('jarvis__bg.jpg')
        image = image.resize((960, 750))
        photo = ImageTk.PhotoImage(image)

        # Create a Label Widget to display the background image
        bl = Label(self, image=photo )
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        # f1 = Frame(self, bg="grey")
        # f1.pack()
        # lblvideo = Label(f1)
        # lblvideo.pack()
        # tkvideo("jarvis_background.mp4", lblvideo, loop=1, size=(200, 130)).play()
        # tkvideo("heading.gif", lblvideo, loop=1, size=(200, 130)).play()
        # Button(f1, text="Stop jarvis", fg="white", bg="red", relief=SUNKEN, borderwidth=4).pack()


if __name__=="__main__":
    jarvis=GUI_AI()
    jarvis.mainloop()
