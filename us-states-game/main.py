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
correct_guessed_answers = []
number_of_all_states = len(all_states)

while len(correct_guessed_answers) < 50:

    if answer_state == "Exit":
        missing_states = []
        for s in all_states:
            if not s in correct_guessed_answers:
                missing_states.append(s)
        new_data_frame = pandas.DataFrame(missing_states)
        new_data_frame.to_csv("learn_states.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_guessed_answers.append(answer_state)

    answer_state = screen.textinput(title=f"{len(correct_guessed_answers)}/{number_of_all_states} States Correct",
                                    prompt="What's another state's name?").title()
