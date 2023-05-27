from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
HIGH_SCORE_FILE = "data.txt"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.setx(0)
        self.goto(0, 260)
        self.score = 0
        self.high_score = 0
        self.get_high_score_from_file()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.save_high_score_to_file()

    def get_high_score_from_file(self):
        with open(HIGH_SCORE_FILE, mode="r") as file:
            self.high_score = file.readline()

    def save_high_score_to_file(self):
        with open(HIGH_SCORE_FILE, mode="w") as file:
            file.write(str(self.high_score))

