from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
tim.pensize(15)
tim.speed(0)


def random_color():
    tim.color(random.choice(colours))


def turn():
    return random.choice([0, 90, 180, 270])


for x in range(200):
    random_color()
    tim.forward(40)
    tim.setheading(turn())
