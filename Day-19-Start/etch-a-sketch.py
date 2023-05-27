from turtle import Turtle, Screen


def move_forward():
    matt.forward(20)


def move_backwards():
    matt.backward(20)


def move_left():
    matt.setheading(matt.heading() + 20)


def move_right():
    matt.setheading(matt.heading() + -20)


def clear_screen():
    matt.clear()
    matt.penup()
    matt.home()
    matt.pendown()


matt = Turtle()
screen = Screen()

# Window is starting to listen for events like key stroke.
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
