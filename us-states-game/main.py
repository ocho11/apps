import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

if answer_state in all_states:
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state_data = data[data.state == answer_state]
    state.goto(int(state_data.x), int(state_data.y))
    state.write(state_data.state.item())

screen.exitonclick()
