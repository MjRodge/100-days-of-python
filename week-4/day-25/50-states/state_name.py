from turtle import Turtle


class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state_name(self, state_x, state_y, state_name):
        self.goto(state_x, state_y)
        self.write(state_name, align="center", font=("Courier", 5, "normal"))
