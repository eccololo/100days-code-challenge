import tkinter as tk
from tkinter.ttk import Label

root = tk.Tk()
root.title("My First Gui Program.")
root.minsize(height=480, width=640)

# Labels
label = Label(root, text="This is my label", font=("Arial", 25, "bold"))
label.pack(expand=True)
root.mainloop()
