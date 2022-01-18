import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

# dashed square created with for nested for loops
for x in range(4):
    for y in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    tim.left(90)

turtle_screen = Screen()
turtle_screen.exitonclick()
