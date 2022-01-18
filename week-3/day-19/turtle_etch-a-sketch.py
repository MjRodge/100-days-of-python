from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    heading = tim.heading() + 10
    tim.setheading(heading)


def turn_right():
    heading = tim.heading() - 10
    tim.setheading(heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
# create screen
turtle_screen = Screen()
# have screen listen for events
turtle_screen.listen()
# keybinding
turtle_screen.onkey(fun=move_forward, key="w")
turtle_screen.onkey(fun=move_backward, key="s")
turtle_screen.onkey(fun=turn_left, key="a")
turtle_screen.onkey(fun=turn_right, key="d")
turtle_screen.onkey(fun=clear_screen, key="c")
turtle_screen.exitonclick()
