from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        if self.xcor() < 380 and self.ycor() < 285:
            self.goto(self.xcor() + 4, self.ycor() + 3)
