import tkinter as tk
from tkinter import messagebox
class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.entry_task = tk.Entry(root, font=("Times New Roman", 16))
        self.entry_task.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.btn_add = tk.Button(root, text="Add Task", command=self.add_task, font=("Times New Roman", 16), bg='#3498DB', fg='white')
        self.btn_add.grid(row=0, column=2, padx=10, pady=5)

        self.listbox_tasks = tk.Listbox(root, font=("Times New Roman", 16), width=40, height=15)
        self.listbox_tasks.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        self.btn_done = tk.Button(root, text="Done", command=self.mark_done, font=("Times New Roman", 16), bg='#2ECC71', fg='white')
        self.btn_done.grid(row=2, column=0, padx=10, pady=5)

        self.btn_delete = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Times New Roman", 16), bg='#E74C3C', fg='white')
        self.btn_delete.grid(row=2, column=1, padx=10, pady=5)

        self.btn_clear = tk.Button(root, text="Clear All", command=self.clear_all_tasks, font=("Times New Roman", 16), bg='#F39C12', fg='white')
        self.btn_clear.grid(row=2, column=2, padx=10, pady=5)

        self.root.configure(bg='#EAF2F8')

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append((task, False))
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.listbox_tasks.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()

    def clear_all_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def mark_done(self):
        selected_task_index = self.listbox_tasks.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task, completed = self.tasks[index]
            self.tasks[index] = (task, True)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.listbox_tasks.delete(0, tk.END)
        for task, completed in self.tasks:
            task_with_status = f"[{'✓' if completed else ' '}] {task}"
            self.listbox_tasks.insert(tk.END, task_with_status)
            self.listbox_tasks.itemconfig(tk.END, foreground="green" if completed else "black")

root = tk.Tk()
root.geometry("500x500")
app = TodoListApp(root)
root.mainloop()