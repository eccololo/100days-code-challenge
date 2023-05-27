from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def score_l(self):
        self.l_score += 1
        self.update_score()

    def score_r(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Arial", 36, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Arial", 36, "normal"))
