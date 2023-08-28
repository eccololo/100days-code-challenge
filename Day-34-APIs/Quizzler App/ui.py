from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.root = Tk()
        self.root.title("Quizzlet")
        self.root.config(pady=20, padx=20, bg=THEME_COLOR)
        self.root.geometry("400x500")

        self.score_label = Label(self.root, text="Score: 0", background=THEME_COLOR,
                                 font=("Arial", 12, "bold"), foreground="white")
        self.score_label.grid(row=0, column=1, sticky='E', pady=10)

        self.question_canvas = Canvas(width=360, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(90, 70, text="Question 1", fill="black", font=("Arial", 20, "italic"))
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=5)

        self.true_btn_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(text="Send", width=13, image=self.true_btn_img,
                          cursor="hand2")
        self.true_btn.grid(row=2, column=0, pady=25)

        self.false_btn_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(text="Send", width=13, image=self.false_btn_img,
                               cursor="hand2")
        self.false_btn.grid(row=2, column=1, pady=25)

        self.root.mainloop()

