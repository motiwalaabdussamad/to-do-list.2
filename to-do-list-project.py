import tkinter as tk
from tkinter import messagebox

from datetime import datetime

def save_task(task):
    with open("to-do-list.txt","a") as file:
        file.write(task + "\n")

def add_task():
    task = task_entry.get()
    new_task = f" {task} [ ]"

    if task:
        task_entry.delete(0,tk.END)
        task_list_box.insert(tk.END,new_task)
        save_task(new_task)
    else:
        messagebox.showwarning("warning ", "task cannot be empty ")

def load_file():
    try:
        with open("to-do-list.txt","r",encoding= "utf-8") as file:
            for line in file:
                task_list_box.insert(tk.END,line.strip())
    except Exception as e :
        print(e)



def remove_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.delete(selected_task)
        save_all_task()
    else:
        messagebox.showwarning("warning","no task selected ")

def clear_all():
    task_list_box.delete(0,tk.END)
    save_all_task()

def mark_complete():
    selected_task_index = task_list_box.curselection()
    if selected_task_index:
        selected_task = task_list_box.get(selected_task_index)
        if selected_task.endswith ("[ ]"):
            completed_task = f"{selected_task[0:-3]}[√] COMPLETED on {datetime.now().strftime("%Y-%M-%D %H-%M-%S")}"
            task_list_box.delete(selected_task_index)
            task_list_box.insert(selected_task_index,completed_task)
            save_all_task()
        else:
            messagebox.showinfo("info ","task is marked as completed ")
    else:
        messagebox.showwarning("warning","no task selected" )

def save_all_task():
    with open("to-do-list.txt","w",encoding="utf-8") as save_file:
        for i in task_list_box.get(0,tk.END):
            print(i)
            save_file.write(i + "\n")





root  = tk.Tk()

root.title("To Do List")
root.geometry("600x600")

main_frame = tk.Frame(root)
main_frame.pack(pady = 20)

task_entry = tk.Entry(main_frame, width = 35)
task_entry.grid(row = 0 , column = 0, pady = 5)

add_button = tk.Button(main_frame,text = "Add Task ", command=add_task)
add_button.grid(row = 0 , column = 1)

task_list_box = tk.Listbox(main_frame, width =60 , height = 15 , selectmode=tk.SINGLE)
task_list_box.grid(row = 1 , column = 0, columnspan= 2,pady = 10)

button_frame = tk.Frame(root)
button_frame.pack(pady = 10)

task_complete = tk.Button(button_frame,text = "mark complete",command=mark_complete)
task_complete.grid(row = 0, column = 0,padx = 10)

task_remove_button = tk.Button(button_frame ,text = "remove task ", command = remove_task)
task_remove_button.grid(row = 0 , column = 1, padx = 10)

clear_task_button = tk.Button(button_frame,text = "clear all ",command=clear_all)
clear_task_button.grid(row = 0 , column = 2, padx = 10)
load_file()

# testing
print("hello")

root.mainloop()




















































