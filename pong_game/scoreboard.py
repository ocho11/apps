from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.player_1_left_score = 0
        self.player_2_right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 200)
        self.write(arg=self.player_1_left_score, align="center", font=("Arial", 50, "normal"))
        self.goto(80, 200)
        self.write(arg=self.player_2_right_score, align="center", font=("Arial", 50, "normal"))

    def increase_player_1_left_score(self):
        self.player_1_left_score += 1
        self.update_scoreboard()

    def increase_player_2_right_score(self):
        self.player_2_right_score += 1
        self.update_scoreboard()
