from turtle import Turtle, Screen
import random

# create screen
turtle_screen = Screen()
turtle_screen.setup(width=500, height=400)
user_choice = turtle_screen.textinput(title="place your bets", prompt="which colour turtle will win?")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_location = [-150, -90, -30, 30, 90, 150]
all_turtles = []

for x in range(0, len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[x])
    new_turtle.goto(x=-230, y=y_location[x])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_choice:
                print(f"you win! the {winning_colour} turtle won the race!")
            else:
                print(f"you lose! the {winning_colour} turtle won the race!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

turtle_screen.exitonclick()
