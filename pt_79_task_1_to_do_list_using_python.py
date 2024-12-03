# 20 22
import tkinter#build_in_library
import tkinter.messagebox#build_in_library
import pickle

window=tkinter.Tk()
window.title("To do list")
window.geometry("700x450")
window.maxsize(700,450)
window.minsize(700,450)
# 22 22
def task_adding():
    todo=task_add.get()
    if todo!="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION !!",message="TO ADD A TASK,PLEASE ENTER SOME TASK !!")

def task_removing():
    try:
        index_todo=list_frame.curselection()[0]
        list_frame.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION !!",message="TO DELETE A TASK,YOU MUST SELECT A TASK !!")

def task_load():
    try:
        todo_list=pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter.END)
        for todo in todo_list:
            list_frame.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION !!",message="CANNOT FIND task.dat !!")

def task_save():
    todo_list=list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("task.dat","wb"))

list_frame=tkinter.Frame(window)
list_frame.pack()

todo_box=tkinter.Listbox(list_frame,height=20,width=110)

todo_box.pack(side=tkinter.LEFT)
scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller)
scroller.config(command=list_frame)

task_add=tkinter.Entry(window,width=110)
task_add.pack()


add_task_button= tkinter.Button(window,text="CLICK TO ADD TASK",font=("arial",8,"bold"),background="blue",width=30,command=task_adding,fg="white")
add_task_button.pack(anchor="n")

remove_task_button=tkinter.Button(window,text="CLICK TO DELETE TASK",font=("arial",8,"bold"),background="red",width=30,command=task_removing,fg="white")
remove_task_button.pack(anchor="n")

load_task_button=tkinter.Button(window,text="CLICK TO LOAD TASK",font=("arial",8,"bold"),background="orange",width=30,command=task_load,fg="white",)
load_task_button.pack(anchor="n")

save_task_button=tkinter.Button(window,text="CLICK TO SAVE TASK",font=("arial",8,"bold"),background="green",width=30,command=task_save,fg="white")
save_task_button.pack(anchor="n")
window.mainloop()
# 18 45

