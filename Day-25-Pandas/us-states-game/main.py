import turtle
import pandas as pd
import time


def get_x_y_coordinates_from_map(x, y):
    """Helper function to get coordinates of US States."""
    print(x, y)


def diff(list1, list2):
    """This simple function show difference between data from list 1 and
    data in list 2."""
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
turtle_writer = turtle.Turtle()

states_df = pd.read_csv(filepath_or_buffer="50_states.csv")
all_states_num = "50"
states_guessed = []
# screen.onscreenclick(get_x_y_coordinates_from_map)

game_is_on = True
while game_is_on:
    player_answer = screen.textinput(title=f"States Guessed: {str(len(states_guessed))}/{all_states_num}.",
                                     prompt="What's another states name?")
    player_answer = player_answer.title()

    if player_answer == "Exit":
        break

    state_series = states_df[states_df["state"] == player_answer]
    if not len(state_series) == 0:
        states_guessed.append(player_answer)
        state_name = state_series["state"].item()
        x_cor = state_series["x"].item()
        y_cor = state_series["y"].item()
        turtle_writer.hideturtle()
        turtle_writer.penup()
        turtle_writer.goto(x_cor, y_cor)
        turtle_writer.write(state_name, font=("Verdana", 12, "bold"), align="center")

    if len(states_guessed) == int(all_states_num):
        turtle_writer.goto(0, 0)
        turtle_writer.write("Brawo! You Win!", font=("Verdana", 15, "bold"), align="center")
        time.sleep(2)
        game_is_on = False

all_states = states_df.state.to_list()
states_to_learn = diff(all_states, states_guessed)
df = pd.DataFrame(states_to_learn, columns=["states"])
df.to_csv("states_to_learn.csv", index=False)
