from tkinter import *
from tkinter.ttk import *
from playsound import playsound

root = Tk()
root.title("Desktop Pass Manager")
root.geometry("520x400")
root.config(pady=50, padx=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    pass


def add_pass():
    www = entry_www.get()
    login = entry_login.get()
    password = entry_pass.get()

    with open("./pass-data.txt", "a") as f:
        f.write(f"{www} | {login} | {password}\n")

    entry_www.delete(0, "")
    entry_pass.delete(0, "")

    playsound("./ping.mp3")


# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(root, width=200, height=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

label_www = Label(root, text="Website: ")
label_www.grid(row=1, column=0)

label_login = Label(root, text="Email / Username: ")
label_login.grid(row=2, column=0)

label_pass = Label(root, text="Password: ")
label_pass.grid(row=3, column=0)

entry_www = Entry(root, width=48)
entry_www.focus()
entry_www.grid(row=1, column=1, columnspan=2)

entry_login = Entry(root, width=48)
entry_login.insert(0, "mateusz@gmail.com")
entry_login.grid(row=2, column=1, columnspan=2)

entry_pass = Entry(root, width=34)
entry_pass.grid(row=3, column=1)

btn_pass = Button(root, text="Generate Pass", command=gen_pass)
btn_pass.grid(row=3, column=2)

btn_add = Button(root, text="Add", command=add_pass, width=48)
btn_add.grid(row=4, column=1, columnspan=2)

root.mainloop()

# ---------------------------- SAVE PASSWORD ------------------------------- #
