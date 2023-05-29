import tkinter as tk
from tkinter.ttk import Label, Button, Entry


def button_clicked():
    user_input = entry.get()
    label["text"] = user_input


root = tk.Tk()
root.title("My First Gui Program.")
root.minsize(height=480, width=640)
root.config(padx=50, pady=50)

# Labels
label = Label(root, text="This is my label", font=("Arial", 25, "bold"))
label.grid(row=0, column=0)
label["text"] = "This is a new text"
label.config(padding=50)

button = Button(text="My Button", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

entry = Entry(width=30)
entry.insert(0, "Enter you username.")
entry.grid(column=3, row=2)

root.mainloop()
