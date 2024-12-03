from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
canvas_widget=Canvas(root,width=canvas_width,height=canvas_height)
canvas_widget.pack()

# The line goes from the point x1,y1 to x2,y2
canvas_widget.create_line(0,0,800,400,fill="red")
canvas_widget.create_line(0,400,800,0,fill="red")
# ctrl +rightclick to see details of any python library.

# To create a rectangle specify parameters in this order - co-ordinate of top left and co-ordinates of bottom right
# canvas_widget.create_rectangle(3,5,700,300,fill="blue")
# canvas_widget.create_text(200,200,text="python")
# canvas_widget.create_oval(344,233,244,355)


# Quick Quiz 6
# Create two canvas widget function which is not explained in this video
# img=PhotoImage(file='2.png')
# canvas_widget.create_image(10,10,image="2.png",anchor=NW)

# canvas_widget.create_window(20,29)
canvas_widget.create_polygon(399,399,399,399,fill="brown")
root.mainloop()