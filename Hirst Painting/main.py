import turtle
import colorgram
from turtle import Screen
import random


def extract_colors_from_image(image_src, num_of_colors):
    """Extracting colors from JPG image."""
    colors = colorgram.extract(image_src, num_of_colors)
    colors_palete = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r, g, b)
        colors_palete.append(color_tuple)

    return colors_palete


def set_initial_turtle_position(my_turtle, my_screen, y_offset):
    my_turtle.penup()
    my_turtle.goto(-my_screen.window_width() / 2 + 50, -my_screen.window_height() / 2 + 20 + y_offset)
    my_turtle.pendown()
    my_turtle.showturtle()


def draw_dotted_line(my_turtle, length, color_palete):
    dash_length = 50
    circle_radius = 15

    for _ in range(int(length / 10)):
        r, g, b = random.choice(color_palete)
        my_turtle.pencolor(r, g, b)
        my_turtle.fillcolor(r, g, b)
        my_turtle.begin_fill()
        my_turtle.circle(circle_radius)
        my_turtle.end_fill()
        my_turtle.penup()
        my_turtle.forward(dash_length)
        my_turtle.pendown()


if __name__ == "__main__":
    color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
                  (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
                  (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
                  (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
                  (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
    matt = turtle.Turtle()
    matt.speed("fastest")
    matt.hideturtle()
    screen = Screen()
    screen.colormode(255)
    screen.setup(550, 550)

    for i in range(45, 451, 45):
        set_initial_turtle_position(matt, screen, i)
        draw_dotted_line(matt, 100, color_list)

    screen.exitonclick()
