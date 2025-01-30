import tkinter as tk
from tkinter import ttk, messagebox

# Create Main Window
root = tk.Tk()
root.title("To-Do List ✅")
root.geometry("450x500")
root.configure(bg="#2C3E50")  # Dark background color

# Task List
tasks = []

# Add Task Function
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        tasks.append(task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Remove Task Function
def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Mark Task as Completed
def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# UI Elements
frame = tk.Frame(root, bg="#34495E")
frame.pack(pady=10)

task_entry = ttk.Entry(frame, width=40, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

# Listbox with Scrollbar
list_frame = tk.Frame(root, bg="#34495E")
list_frame.pack(pady=10)

task_listbox = tk.Listbox(list_frame, width=50, height=12, font=("Arial", 12), bg="#ECF0F1", fg="black")
task_listbox.pack(side=tk.LEFT)

scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = tk.Frame(root, bg="#34495E")
button_frame.pack(pady=10)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=0, padx=5)

complete_button = ttk.Button(button_frame, text="Mark as Completed", command=mark_completed)
complete_button.grid(row=0, column=1, padx=5)

exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

# Run Application
root.mainloop()