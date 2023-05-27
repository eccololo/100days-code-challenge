from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game by Mateusz Hyla")
screen.tracer(0)

left_paddle = Paddle((-330, 0))
right_paddle = Paddle((330, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detection of collision with upper and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce from wall
        ball.bounce_y()

    # Detecting collision with right paddle.
    if (ball.distance(right_paddle) <= 50 and ball.xcor() >= 320) or\
            (ball.distance(left_paddle) <= 50 and ball.xcor() <= -320):
        ball.bounce_x()

    # Detect if ball go beyond right paddle.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_l()

    # Detect if ball go beyond right left.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_r()

screen.exitonclick()
