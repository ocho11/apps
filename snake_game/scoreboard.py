from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
DATA = "data.txt"


def get_high_score_form_data():
    with open(DATA) as file:
        return file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(get_high_score_form_data())
        self.color("White")
        self.penup()
        self.goto(10, 270)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}        High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA, mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
