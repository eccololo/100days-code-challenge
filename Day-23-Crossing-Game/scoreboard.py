from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 1
        self.write("Level: {}".format(self.level), align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-200, 250)
        self.write("Level: {}".format(self.level), align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 44, "normal"))
