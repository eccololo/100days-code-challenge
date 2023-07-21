from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
import random
import csv


DATA_FILE_PATH = "assets/data/300_italian_polish_most_common_words.csv"

root = Tk()
root.title("Flash Cards App")
root.geometry("620x500")
root.config(pady=50, padx=50)

root.mainloop()