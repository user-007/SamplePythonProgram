from datetime import time
from turtle import Turtle, Screen

from ping_pong.main import game_is_on
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()


screen.listen()
screen.onkey(player.go_up, "Up")

gone_is_on = True
while game_is_on:
    time.sleep(0, 1)
    screen.update()

    car_manager.create_url()
    car_manager.move_cars()

