from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)
