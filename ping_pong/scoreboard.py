from turtle import Turtle
from paddle import Paddle
from ball import Ball

import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto()
        self.write(self.l_score, align="center", Font=("Courirer", 80))
