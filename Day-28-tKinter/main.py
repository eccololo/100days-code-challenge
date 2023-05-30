from tkinter import *
from tkinter.ttk import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#11009E"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro App")
root.config(pady=50, padx=100, bg=YELLOW)

label_1 = Label(text="Timer", font=(FONT_NAME, 25, "bold"), background=YELLOW, foreground=GREEN)
label_1.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

style = Style()
style.configure('W.TButton', font=(FONT_NAME, 11, 'bold'), foreground=BLUE)

start_btn = Button(text="Start", command=start, style="W.TButton")
start_btn.grid(row=2, column=0)

start_btn = Button(text="Reset", command=reset, style="W.TButton")
start_btn.grid(row=2, column=2)

root.mainloop()
