import time
from turtle import Screen
from player import Player, player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle_crossing_point import car_manager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

for car in car_manager.all_cars:
   if car.distance(player) < 20:
       game_is_on  = False
# Detect successful processing
if player.is_at_finish_line():
    player.go_to_start()
    car_manager.level_up()


screen.exitonclick()
