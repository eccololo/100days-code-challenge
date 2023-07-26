# TODO:
#    5. Zrobic tak aby po przerobieniu wszystkich pytan pojawil sie komunikat z gratulacjami.


from functools import partial
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
import random
import csv
import sys

DATA_FILE_PATH = "assets/data/300_italian_polish_most_common_words.csv"
DATA_SET = None
FONT_NAME = "Courier"
CANVAS_BG_COLOR = "#74b291"
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 550
TIMER = None
QUESTION_NO = None
QUESTION_NO_MAX = 300
TITLE = None
QA = None
CANVAS = None
IMAGE_TAG = None
COUNT_DOWN_TIME = 7000


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
def clear_canvas_writing_field():
    """This function clear what is written on canvas."""
    CANVAS.delete(TITLE)
    CANVAS.delete(QA)


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
    global TITLE, QA, QUESTION_NO
    QUESTION_NO = random.randrange(2, QUESTION_NO_MAX)

    clear_canvas_writing_field()
    subject_front = DATA_SET[1]["question"]
    question = DATA_SET[QUESTION_NO]["question"]
    TITLE = CANVAS.create_text(290, 100, text=f"{subject_front}", fill="black", font=(FONT_NAME, 30, "bold"))
    QA = CANVAS.create_text(300, 210, text=f"{question}", fill="black", font=(FONT_NAME, 55, "bold"))
    count_down(root)


def show_next_question_if_true():
    """This function showes user next question if he guest previous one. It decrease number of questions.
    if user guest previous one."""
    global TITLE, QA, QUESTION_NO, QUESTION_NO_MAX

    del DATA_SET[QUESTION_NO]
    QUESTION_NO_MAX -= 1
    QUESTION_NO = random.randrange(2, QUESTION_NO_MAX)
    playsound("./assets/sounds/notification.mp3")

    clear_canvas_writing_field()
    subject_front = DATA_SET[1]["question"]
    question = DATA_SET[QUESTION_NO]["question"]
    TITLE = CANVAS.create_text(290, 100, text=f"{subject_front}", fill="black", font=(FONT_NAME, 30, "bold"))
    QA = CANVAS.create_text(300, 210, text=f"{question}", fill="black", font=(FONT_NAME, 55, "bold"))
    count_down(root)


def show_next_question_if_false():
    """This function showes user next question when he don't know the answer and play sound
    when button is clicked."""
    playsound("./assets/sounds/notification.mp3")
    show_next_question()


def count_down(root):
    """This function counts 5 seconds and then execute flip to answer function. """
    global TIMER
    flip_to_answer_partial = partial(flip_to_answer, root)
    TIMER = root.after(COUNT_DOWN_TIME, flip_to_answer_partial)


def flip_to_answer(root):
    """This function flips flash card to show answer."""
    global TIMER, CANVAS, IMAGE_TAG, QA, TITLE
    clear_canvas_writing_field()
    root.after_cancel(TIMER)

    subject_back = DATA_SET[1]["answer"]
    answer = DATA_SET[QUESTION_NO]["answer"]
    TITLE = CANVAS.create_text(290, 100, text=f"{subject_back}", fill="black", font=(FONT_NAME, 30, "bold"))
    QA = CANVAS.create_text(300, 210, text=f"{answer}", fill="black", font=(FONT_NAME, 55, "bold"))


root = Tk()
root.title("Flash Cards App")
center_the_project_window(root)
root.config(pady=40, padx=40)
root.configure(bg='#B1DDC6')

DATA_SET = return_question_answer_from_data_set()

# ======================= UI ===========================
CANVAS = Canvas(root, width=625, height=395, bg=CANVAS_BG_COLOR, highlightthickness=0)
flash_card_image = PhotoImage(file="./assets/images/card_front.png")
IMAGE_TAG = CANVAS.create_image(230, 140, image=flash_card_image)
CANVAS.grid(column=0, row=0, columnspan=2)
TITLE = CANVAS.create_text(290, 100, text="Italian", fill="black", font=(FONT_NAME, 30, "bold"))
QA = CANVAS.create_text(300, 210, text="Question", fill="black", font=(FONT_NAME, 55, "bold"))

false_image = PhotoImage(file="./assets/images/wrong.png")
false_btn = Button(image=false_image, command=show_next_question_if_false)
false_btn.grid(row=1, column=0)

right_image = PhotoImage(file="./assets/images/right.png")
right_btn = Button(image=right_image, command=show_next_question_if_true)
right_btn.grid(row=1, column=1)

show_next_question()
count_down(root)

root.mainloop()
