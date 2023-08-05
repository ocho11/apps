import turtle as game
from paddle import Paddle

screen = game.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

player_1 = Paddle()

game.listen()
game.onkey(fun=player_1.up, key="Up")
game.onkey(fun=player_1.down, key="Down")

screen.exitonclick()
