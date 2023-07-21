from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
import random
import csv

DATA_FILE_PATH = "assets/data/300_italian_polish_most_common_words.csv"
FONT_NAME = "Courier"
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 550


# ===================== Utilities ===============
def center_the_project_window(w_root):
    """This function centers app window of the center of the screen when it is open. Code taken from
    StackOver Flow."""
    w = WINDOW_WIDTH  # width for the Tk root
    h = WINDOW_HEIGHT  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    w_root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = Tk()
root.title("Flash Cards App")
center_the_project_window(root)
root.config(pady=40, padx=40)
root.configure(bg='#B1DDC6')

# ======================= UI ===========================
canvas = Canvas(root, width=625, height=395, bg='#B1DDC6', highlightthickness=0)
logo_image = PhotoImage(file="./assets/images/card_front.png")
canvas.create_image(230, 140, image=logo_image)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(290, 100, text="Italian", fill="black", font=(FONT_NAME, 30, "bold"))
question_word = canvas.create_text(300, 210, text="Question", fill="black", font=(FONT_NAME, 55, "bold"))

root.mainloop()
