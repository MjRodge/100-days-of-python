from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

sides = 3
while sides <= 20:
    side_angle = 360/sides
    tim.color(random.choice(colours))
    for x in range(sides):
        tim.forward(100)
        tim.right(side_angle)
    sides += 1


screen = Screen()
screen.exitonclick()
