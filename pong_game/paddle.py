import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350, 0)
        turtle.update()
        self.speed("fastest")

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)
            turtle.update()

    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)
            turtle.update()
