from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
from random import randint, shuffle, choice
import pyperclip
import re

DB_PASS_FILE_PATH = "./pass-data.txt"

root = Tk()
root.title("Desktop Pass Manager")
root.geometry("520x400")
root.config(pady=50, padx=50)


# ---------------------------- UTILITIES ------------------------------- #

def check_for_duplicates(**kwargs):
    """This function checks if typed by user www and login already exists in DB."""
    www = kwargs["www"]
    login = kwargs["login"]

    with open(DB_PASS_FILE_PATH, "r") as f:
        data = f.readlines()

    cleaned = list(map(lambda x: x.replace("\n", ""), data))
    for item in cleaned:
        if www in item and login in item:
            return True

    return False


def override_pass(**kwargs):
    """This function update user password if duplicate entry is detected if user wants to."""
    www = kwargs["www"]
    login = kwargs["login"]
    password = kwargs["password"]
    output = ""

    with open(DB_PASS_FILE_PATH, "r") as f:
        data = f.readlines()

    cleaned = list(map(lambda x: x.replace("\n", ""), data))
    for item in cleaned:
        if len(item) > 0:
            splitted = item.split("|")
            db_www = splitted[0].strip()
            db_login = splitted[1].strip()
            db_pass = splitted[2].strip()
            if db_www == www and db_login == login:
                db_pass = password
                output += f"{db_www} | {db_login} | {db_pass}\n"
            else:
                output += f"{db_www} | {db_login} | {db_pass}\n"

    with open(DB_PASS_FILE_PATH, "w") as f:
        f.write(output)


def clear_entries_labels():
    """This is helper function that clear entries and labels from values."""
    entry_www.delete(0, END)
    entry_pass.delete(0, END)
    label_copied.config(text="")


# ---------------------------- DATA VALIDATION ------------------------------- #

def validate_data(**kwargs):
    """This function checks the corectness of entered by user data."""
    pattern_www = "[a-zA-Z0-9]+\\.[a-zA-Z0-9]{2,5}"

    if len(kwargs["www"]) == 0:
        messagebox.showwarning(title="Website Empty!", message="Website address cannot be empty!")
        return False
    elif not re.match(pattern_www, kwargs["www"]):
        messagebox.showwarning(title="Wrong Website!", message="Website address is incorrect!")
        return False
    elif len(kwargs["login"]) == 0:
        messagebox.showwarning(title="Login Empty!", message="Login cannot be empty!")
        return False
    elif len(kwargs["password"]) == 0:
        messagebox.showwarning(title="Password Empty!", message="Password cannot be empty!")
        return False

    return True


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    """This function generate strong password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 11))]
    password_list += [choice(symbols) for _ in range(randint(3, 4))]
    password_list += [choice(numbers) for _ in range(randint(3, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    entry_pass.insert(0, password)

    pyperclip.copy(password)

    label_copied.config(text="Copied!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    """This function saves enetred data by user to DB like www, login and password."""
    www = entry_www.get()
    login = entry_login.get()
    password = entry_pass.get()

    duplicate_proceed = False
    is_duplicates = check_for_duplicates(www=www, login=login)

    if is_duplicates:
        duplicate_proceed = messagebox.askyesno(title="Duplicated Detected!",
                                                message="This website address and login are already in database. Do you want to update your pass?")

    if is_duplicates:
        override_pass(www=www, login=login, password=password)
        messagebox.showinfo(title="Success!", message="Password updated!")
        clear_entries_labels()

    elif not duplicate_proceed:
        is_data_ok = validate_data(www=www, login=login, password=password)

        if is_data_ok:

            is_ok = messagebox.askokcancel(title=www, message=f"Details:\nlogin: {login}\npassword: {password}\n"
                                                              f"Is it ok to save?")

            if is_ok:
                with open(DB_PASS_FILE_PATH, "a") as f:
                    f.write(f"{www} | {login} | {password}\n")

                clear_entries_labels()
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

label_copied = Label(root, text="")
label_copied.grid(row=3, column=3)

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
