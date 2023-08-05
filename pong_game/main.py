import turtle as game
from paddle import Paddle
from ball import Ball
import time

screen = game.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1_right = Paddle((350, 0))
player_2_left = Paddle((-350, 0))
ball = Ball()

game.listen()
game.onkey(fun=player_1_right.up, key="Up")
game.onkey(fun=player_2_left.up, key="w")
game.onkey(fun=player_1_right.down, key="Down")
game.onkey(fun=player_2_left.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
