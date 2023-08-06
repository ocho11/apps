from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.score_update()

    def score_update(self):
        self.penup()
        self.goto(-230, 250)
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)