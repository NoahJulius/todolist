import tkinter as tk

root = tk.Tk()
root.geometry("500x450")
root.title("to do list")
root.config(bg= 'black')

frame = tk.Frame(root)
frame.pack(pady=10)

tasks_list = tk.Listbox(frame, width=25, height=8, font=('Times', 18),
                    fg='#464646', selectbackground='#333333', activestyle='none')
tasks_list.pack(side=tk.LEFT, fill=tk.BOTH)

scroll_bar = tk.Scrollbar(frame).pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_list.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=tasks_list.yview)

task_entry = tk.Entry(root, font=('Times', 24))
task_entry.insert(0, 'enter task')
task_entry.pack(pady=20)

root.mainloop()

