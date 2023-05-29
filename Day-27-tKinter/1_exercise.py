import tkinter as tk
from tkinter.ttk import Label, Button, Entry

root = tk.Tk()
root.title("My First Gui Program.")
root.minsize(height=480, width=640)

# Labels
label = Label(root, text="This is my label", font=("Arial", 25, "bold"))
label.pack(expand=True)
label["text"] = "This is a new text"


def button_clicked():
    user_input = entry.get()
    label["text"] = user_input


button = Button(text="My Button", command=button_clicked)
button.pack(expand=True)

entry = Entry(width=30)
entry.pack(expand=True)

root.mainloop()
