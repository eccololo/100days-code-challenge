import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


def create_or_increase_list_of_cars():
    random_x = random.randint(300, 900)
    random_y = random.randint(-260, 240)
    list_of_cars.append(CarManager(random_x, random_y))


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

list_of_cars = []
for _ in range(30):
    create_or_increase_list_of_cars()

screen.listen()
screen.onkey(player.move_player_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(list_of_cars[0].get_car_speed())
    screen.update()

    # Moving cars and restarting its position
    for car in list_of_cars:
        car.car_move()
        car.restart_car()

    # We go to next level, increase car speed and add extra cars after every next level
    if player.next_level():
        scoreboard.next_level()
        # increasing num of cars.
        for _ in range(5):
            create_or_increase_list_of_cars()
        # increasing cars speed and restarting its position.
        for car in list_of_cars:
            car.increase_car_speed()

    # If player hits car.
    for car in list_of_cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            time.sleep(5)
            game_is_on = False
