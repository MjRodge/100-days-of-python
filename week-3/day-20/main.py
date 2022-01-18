from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek.")
screen.tracer(0)

snake_body = []
x_coord = 0


for x in range(0, 3):
    new_body_section = Turtle(shape="square")
    new_body_section.penup()
    new_body_section.color("white")
    new_body_section.goto(x=x_coord, y=0)
    snake_body.append(new_body_section)
    x_coord = x_coord-20

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    for section in range(len(snake_body)-1, 0, -1):
        new_x_coord = snake_body[section-1].xcor()
        new_y_coord = snake_body[section-1].ycor()
        snake_body[section].goto(new_x_coord, new_y_coord)
    snake_body[0].forward(20)








screen.exitonclick()