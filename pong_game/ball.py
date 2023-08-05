from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_horizontal()
