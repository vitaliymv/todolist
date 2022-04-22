# --------------------Imports-------------------------
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import Calendar
# --------------------Imports-------------------------


# ----------------Tkinter configures------------------
from task import Task

screen = Tk()
screen.title("To-Do List")
screen.geometry("1000x800")
# ----------------Tkinter configures------------------


# -------------------Variables------------------------
current_datetime = datetime.now()
task_list = []
# -------------------Variables------------------------


# -------------------Widgets--------------------------
l1 = Label(screen, text="To-Do List", font=("Arial", 20))
l2 = Label(screen, text="Enter task title", font=("Arial", 20))
task_entry = Entry(screen, width=18, font=("Arial", 20))
task_box = Listbox(screen, height=12, width=50, selectmode="SINGLE", bd=4, font=("Arial", 15))
b1 = Button(screen, text="Add task", width=20, font=("Arial", 17), command=lambda: add_task())
b2 = Button(screen, text="Delete", width=15, font=("Arial", 15))
b3 = Button(screen, text="Delete All", width=15, font=("Arial", 15))
b4 = Button(screen, text="Done", width=15, font=("Arial", 15))
cal = Calendar(screen, selectmode="day",
               year=current_datetime.year,
               month=current_datetime.month,
               day=current_datetime.day, font=("Arial", 15))
b5 = Button(screen, text="Sort", width=10, font=("Arial", 15))
combo = ttk.Combobox(screen, values=["title", "status", "deadline"], font=("Arial", 15), width=10)
combo.current(0)
# -------------------Widgets--------------------------


# ------------------Place Geometry--------------------
l1.place(x=450, y=10)
l2.place(x=200, y=130)
task_entry.place(x=150, y=180)
task_box.place(x=250, y=400)
b1.place(x=150, y=230)
b2.place(x=630, y=700)
b3.place(x=250, y=700)
b4.place(x=50, y=500)
cal.place(x=550, y=100)
b5.place(x=820, y=550)
combo.place(x=820, y=500)
# ------------------Place Geometry--------------------


# --------------------Functions-----------------------
def add_task():
    word = task_entry.get()
    deadline = cal.selection_get()
    if len(word) == 0:
        messagebox.showwarning("Empty entry", "Enter task name")
    else:
        item = Task(word, deadline, False)
        task_list.append(item)
        task_entry.delete(0, "end")

    for i in task_list:
        print(i.title)
        print(i.deadline)
        print(i.status)
        print()
# --------------------Functions-----------------------



screen.mainloop()