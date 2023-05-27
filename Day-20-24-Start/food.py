from turtle import Turtle
import random

FOOD_SHAPES = ["circle", "triangle", "square"]
FOOD_COLORS = ["red", "blue", "green"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(FOOD_SHAPES))
        self.color(random.choice(FOOD_COLORS))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)

        self.refresh_food_shape_color()

        # If food position is on a scoreboard we roll food position again.
        if 5 > random_x > -5 and 265 > random_y > 255:
            random_x = random.randint(-270, 270)
            random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    def refresh_food_shape_color(self):
        self.shape(random.choice(FOOD_SHAPES))
        self.color(random.choice(FOOD_COLORS))
