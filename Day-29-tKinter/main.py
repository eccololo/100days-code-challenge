from tkinter import *
from tkinter.ttk import *
from playsound import playsound

root = Tk()
root.title("Desktop Pass Manager")
root.geometry("280x290")
root.config(pady=20, padx=20)

canvas = Canvas(root, width=200, height=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(120, 120, image=logo_image)
canvas.grid(column=0, row=0)

root.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #