import turtle as game
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = game.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1_left = Paddle((350, 0))
player_2_right = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game.listen()
game.onkey(fun=player_1_left.up, key="Up")
game.onkey(fun=player_2_right.up, key="w")
game.onkey(fun=player_1_left.down, key="Down")
game.onkey(fun=player_2_right.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    if ball.distance(player_1_left) < 50 and ball.xcor() > 320 or ball.distance(
            player_2_right) < 50 and ball.xcor() < -320:
        ball.bounce_horizontal()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increase_player_2_right_score()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increase_player_1_left_score()

    ball.move()

screen.exitonclick()
