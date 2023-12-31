import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.cars_speed)
    screen.update()

    if player.ycor() > player.finish_line:
        player.go_to_start_position()
        scoreboard.level_up()
        car_manager.cars_speed *= 0.8

    if len(car_manager.all_cars) == 0:
        car_manager.create_cars()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
