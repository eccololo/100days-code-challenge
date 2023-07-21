from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
import random
import csv


DATA_FILE_PATH = "assets/data/300_italian_polish_most_common_words.csv"
FONT_NAME = "Courier"

root = Tk()
root.title("Flash Cards App")
root.geometry("720x550")
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