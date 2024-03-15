import TaskManager
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

tasks : list[TaskManager.Task.Task] = []
manager = TaskManager.TaskManager(tasks)

manager.load('tasks.json')

window = Tk()
window.configure(bg="black")
window.title("Task Manager")
window.columnconfigure(0, minsize=500)
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=80)

def add() :
    title = simpledialog.askstring("Titre de la tache", "Entrez le titre")
    description = simpledialog.askstring("Description de la tache", "Entrez la description")
    due_date = simpledialog.askstring("Date de rendu de la tache", "Entrez la date de rendu")
    priority = simpledialog.askinteger("Priorite de la tache", "Entrez la priorite")

    add_window = Toplevel(window)
    add_window.configure(bg="black")
    add_window.title("Task Manager")
    add_window.columnconfigure(0, minsize=500)
    add_window.rowconfigure([0, 1, 2], minsize=80)

    def yes() :
        newTask = TaskManager.Task.Task(title,description,due_date,True,priority)
        manager.add(newTask)
        add_window.destroy()

    def no() :
        newTask = TaskManager.Task.Task(title,description,due_date,True,priority)
        manager.add(newTask)
        add_window.destroy()

    frame = Frame(add_window)
    frame.pack()

    text = Label(frame,
        text="Est-elle complete ?",
        font=20,
        height=2,
        foreground="#FF3030",
        background="black",
        )
    text.grid(row=0, column=0, sticky="nsew")
    no_button = Button(frame,
        text="No",
        width=25,
        height=2,
        background="#FF3030",
        foreground="black",
        command=no
    )
    no_button.grid(row=1, column=0)
    yes_button = Button(frame,
        text="Yes",
        width=25,
        height=2,
        background="#FF3030",
        foreground="black",
        command=yes
    )
    yes_button.grid(row=2, column=0)

    add_window.mainloop()

def delete() :
    task_to_delete = simpledialog.askinteger("Titre de la tache", "Entrez le titre")
    if (task_to_delete > manager.get_number_of_tasks() or task_to_delete < 1) :
        messagebox.showerror("Erreur", "Cette tache n'existe pas")
    else :
        manager.delete(task_to_delete-1)
        messagebox.showinfo("Reussite", "La tache a ete effacee")

def show() :
    show_window = Toplevel(window)
    show_window.configure(bg="black")
    show_window.title("Task Manager")
    show_window.columnconfigure(0, minsize=500)
    show_window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=80)

    frame = Frame(show_window)
    frame.pack()

    show_label = Label(frame,
        text=manager.show_with_string(),
        font=5,
        width=30,
        foreground="#FF3030",
        background="black",
        )
    show_label.grid(row=0, column=0, sticky="nsew")

    show_window.mainloop()

def quit() :
    manager.save()
    window.destroy()

greeting = Label(
    text="Task Manager",
    font=20,
    foreground="#FF3030",
    background="black",
    )
greeting.grid(row=0, column=0, sticky="nsew")
add = Button(
    text="Add a new task",
    width=25,
    height=2,
    background="#FF3030",
    foreground="black",
    command=add
)
add.grid(row=1, column=0)
delete = Button(
    text="Delete an existing task",
    width=25,
    height=2,
    background="#FF3030",
    foreground="black",
    command=delete
)
delete.grid(row=2, column=0)
show = Button(
    text="Show tasks",
    width=25,
    height=2,
    background="#FF3030",
    foreground="black",
    command=show
)
show.grid(row=3, column=0)
quit = Button(
    text="Save and Quit",
    width=25,
    height=2,
    background="#FF3030",
    foreground="black",
    command=quit
)
quit.grid(row=4, column=0)

window.mainloop()