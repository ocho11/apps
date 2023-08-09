import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
data = pandas.read_csv("50_states.csv")
states_name_lower_case = data
all_states = data.state.to_list()
number_of_correct_answer = 0
number_of_all_states = len(all_states)

while number_of_correct_answer < 50:

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        number_of_correct_answer += 1

    answer_state = screen.textinput(title=f"{number_of_correct_answer}/{number_of_all_states} States Correct",
                     prompt="What's another state's name?").title()
