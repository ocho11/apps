from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", False, align=ALIGNMENT, font=FONT)