from turtle import Turtle
import random


class SpecialEffects(Turtle):

    def __init__(self, food):
        super().__init__()
        self.shape(food.shape())
        self.color(food.color()[0])
        self._x = food.xcor() + 20
        self._y = food.ycor() + 20
        self.penup()
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.speed("fastest")
        self.goto(self._x, self._y)

    def mark_food_eaten(self, food):
        self.penup()
        self.shape(food.shape())
        self.color(food.color()[0])
        self._x = food.xcor() + 20
        self._y = food.ycor() + 20
        self.goto(self._x, self._y)
