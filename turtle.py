from turtle import Turtle, colormode, Screen
import random

colormode(255)
t1 = Turtle()
t1.speed(0)
def random_color():
    r = random.randint(0 ,255)
    g  = random.randint(0, 255)
    b = random.randint(0, 255)
