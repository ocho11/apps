import turtle
from paddle import Paddle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

player_1 = Paddle()

turtle.listen()
turtle.onkey(fun=player_1.up, key="Up")
turtle.onkey(fun=player_1.down, key="Down")

screen.exitonclick()
