import turtle
import pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("50 states guessing game")

# configure turtle image background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# load state data
state_data = pandas.read_csv("50_states.csv")
# add state names to list for easy searching with user input
state_list = state_data["state"].to_list()


guessed_all_50 = False
total_guessed_correctly = 0
correct_guesses = []
while not guessed_all_50:
    # get state guess from user
    answer = screen.textinput(title=f"{total_guessed_correctly}/50 states correctly guessed", prompt="guess a state").title()
    # check if guessed state answer is in state_list data
    if answer in state_list:
        total_guessed_correctly += 1
        correct_guesses.append(answer)
        # locate the x and y coordinates of guessed state and convert to list
        state_x = state_data.loc[state_data["state"] == answer, "x"].to_list()
        state_y = state_data.loc[state_data["state"] == answer, "y"].to_list()
        # create a turtle to write to the map
        state_name_writer = StateName()
        # turtle function to write to map location
        state_name_writer.write_state_name(state_x=state_x[0], state_y=state_y[0], state_name=answer)

screen.exitonclick()
