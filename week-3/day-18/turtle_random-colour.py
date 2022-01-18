import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed(0)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def turn():
    return random.choice([0, 90, 180, 270])


for x in range(200):
    tim.color(random_colour())
    tim.forward(40)
    tim.setheading(turn())
