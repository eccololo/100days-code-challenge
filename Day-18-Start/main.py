import turtle
from turtle import Turtle, Screen
import random


def draw_a_square(my_turtle):
    """This function draws a square in Turtle window."""
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


def draw_a_dashed_line(length, my_turtle):
    """This function draws a dashed line."""
    dash_length = 10

    for _ in range(int(length / 10)):
        my_turtle.forward(dash_length)
        my_turtle.penup()
        my_turtle.forward(dash_length)
        my_turtle.pendown()


def draw_a_shape(number_of_sides, side_length, my_turtle):
    angle = int(360 / number_of_sides)
    for j in range(number_of_sides):
        my_turtle.forward(side_length)
        my_turtle.right(angle)


def draw_a_shapes(side_length, my_turtle):
    """This function draws a shapes inside each other in random color."""
    colors = ["cyan", "brown", "blue", "azure", "coral", "green", "red", "tan", "wheat"]
    for i in range(3, 8):
        my_turtle.color(random.choice(colors))
        draw_a_shape(i, side_length, my_turtle)


def gen_random_color():
    """This function generates a random tuple with rgb colors values."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


def random_walk(my_turtle):
    """This function do a random walk."""
    # colors = ["cyan", "brown", "blue", "azure", "coral", "green", "red", "tan", "wheat"]
    line_length = 20
    my_turtle.pensize(10)
    my_turtle.speed("fast")
    turtle.colormode(255)
    list_of_movements = [my_turtle.forward, my_turtle.backward]
    list_of_turns = [my_turtle.right, my_turtle.left]
    while True:
        movement = random.choice(list_of_movements)
        turn = random.choice(list_of_turns)
        # color = random.choice(colors)
        my_turtle.color(gen_random_color())
        movement(line_length)
        turn(random.choice([90, -90]))


def draw_a_spirograph(my_turtle, size_of_gap):
    """This function draws a spirograph in a turtle window."""
    my_turtle.color("black")
    my_turtle.speed("fastest")
    my_turtle.pensize(3)
    turtle.colormode(255)
    circle_radius = 100
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(gen_random_color())
        my_turtle.circle(circle_radius)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


matt = Turtle()
matt.hideturtle()
matt.shape("turtle")
matt.color("cyan")
# draw_a_square(matt)
# draw_a_dashed_line(100, matt)
# draw_a_shape(4, 70, matt)
# draw_a_shapes(70, matt)
# random_walk(matt)
draw_a_spirograph(matt, 10)

screen = Screen()
screen.exitonclick()
