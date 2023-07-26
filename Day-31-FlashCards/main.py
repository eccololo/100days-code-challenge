# TODO:
#    2. Zrobić timer tak aby po 5 sekundach karta flipowala sie na odpowiedz. Dane pobierane z data-set.
#    3. Zrobic tak aby po flipie na odpowiedz timer przestawal odliczac i program czekal na odpowiedz usera.


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
import random
import csv
import inspect
import sys

DATA_FILE_PATH = "assets/data/300_italian_polish_most_common_words.csv"
DATA_SET = None
FONT_NAME = "Courier"
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 550


# ===================== Data ====================
def return_question_answer_from_data_set():
    """This function gets next question and answer from data-set file and returns it."""
    csvfile = None
    reader = None
    data_set = {}
    counter = 1
    try:
        csvfile = open(DATA_FILE_PATH, "r", encoding='utf-8')
        reader = csv.reader(csvfile, delimiter=',')
    except FileNotFoundError:
        messagebox.showinfo("Error.", "Sorry, but DB file with answers and question was not found.\nContact developer.")
        sys.exit()
    finally:
        for row in csvfile:
            question = row.split(",")[0].replace("\n", "")
            answer = row.split(",")[1].replace("\n", "")
            data_set[counter] = {"question": question, "answer": answer}
            counter += 1

        csvfile.close()
        return data_set


# ===================== Utilities ===============
def clear_canvas_writing_field(title, q_a_txt):
    """This function clear what is written on canvas."""
    canvas.delete(title)
    canvas.delete(q_a_txt)


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


# ===================== FUNCTIONALITY ===============
def show_next_question():
    """This function shows on GUI next question. Takes data from data-set."""

    subject_front = DATA_SET[1]["question"]
    subject_back = DATA_SET[1]["answer"]
    question_no = 2
    question = DATA_SET[question_no]["question"]
    answer = DATA_SET[question_no]["answer"]
    canvas.create_text(290, 100, text=f"{subject_front}", fill="black", font=(FONT_NAME, 30, "bold"))
    canvas.create_text(300, 210, text=f"{question}", fill="black", font=(FONT_NAME, 55, "bold"))


root = Tk()
root.title("Flash Cards App")
center_the_project_window(root)
root.config(pady=40, padx=40)
root.configure(bg='#B1DDC6')

DATA_SET = return_question_answer_from_data_set()

# ======================= UI ===========================
canvas = Canvas(root, width=625, height=395, bg='#B1DDC6', highlightthickness=0)
logo_image = PhotoImage(file="./assets/images/card_front.png")
canvas.create_image(230, 140, image=logo_image)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(290, 100, text="Italian", fill="black", font=(FONT_NAME, 30, "bold"))
question_word = canvas.create_text(300, 210, text="Question", fill="black", font=(FONT_NAME, 55, "bold"))

false_image = PhotoImage(file="./assets/images/wrong.png")
false_btn = Button(image=false_image)
# false_btn.config(highlightthickness=0, borderwidth=0)
false_btn.grid(row=1, column=0)

right_image = PhotoImage(file="./assets/images/right.png")
right_btn = Button(image=right_image)
right_btn.grid(row=1, column=1)

clear_canvas_writing_field(title, question_word)
show_next_question()

root.mainloop()
