from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, random_x, random_y):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.car_speed = 0.1
        self.x_speed = 5
        self.goto(random_x, random_y)

    def car_move(self):
        self.setx(self.xcor() - self.x_speed)

    def restart_car(self):
        if self.xcor() <= -310:
            self.setx(random.randint(300, 900))

    def increase_car_speed(self):
        self.car_speed *= 0.9

    def get_car_speed(self):
        return self.car_speed
