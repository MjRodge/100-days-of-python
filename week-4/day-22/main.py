from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# initial screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong.")
screen.tracer(0)

# initial right and left paddle setup
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
# initial ball setup
ball = Ball()
# initial scoreboard setup
scoreboard = Scoreboard()


# keybindings
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "a")
screen.onkey(left_paddle.go_down, "z")

# game animation control
game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()

    # detect wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # detect right_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        # add point to left_paddle scoreboard
        scoreboard.l_point()

    # detect left_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        # add point to right_paddle scoreboard
        scoreboard.r_point()

screen.exitonclick()
