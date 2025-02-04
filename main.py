import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("50_states.csv")

def place_state(state_name , x_cor , y_cor):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto((x_cor , y_cor))
    tim.write(state_name)

correct_answers = []

while len(correct_answers) < 50:
    answer = turtle.textinput(title=f"{len(correct_answers)}/50 States Correct" , prompt="What's another state? ").title()

    if answer == "Exit":
        remaining_states = [state for state in state_data["state"].to_list() if state not in correct_answers]
        # for state in state_data["state"].to_list():
        #     if state not in correct_answers:
        #         remaining_states.append(state)
        remaining_states_dataframe = pd.DataFrame({"Remaining States" : remaining_states})
        remaining_states_dataframe.to_csv("states_to_learn.csv")
        break

    if answer in state_data["state"].to_list():
        if answer not in correct_answers:
            correct_answers.append(answer)

        current_state_data = state_data[state_data.state == answer]
        xcor = current_state_data.x.item()                               #to get item instead of object
        ycor = current_state_data.y.item()
        place_state(answer, xcor, ycor)

