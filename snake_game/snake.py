from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.increase_segment(position)

    def increase_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("White")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def update_snake_length(self):
        self.increase_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg - 1].xcor()
            y_position = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_position, y_position)
        self.head.forward(MOVE_DISTANCE)
