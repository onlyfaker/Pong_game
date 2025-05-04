from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score_count_player1 = 0
        self.score_count_player2 = 0
        self.write(f"{self.score_count_player1}        {self.score_count_player2}",
                   align="center", font=("Verdana", 25, "normal"))

    def increase_score(self):
        self.clear()
        self.write(f"{self.score_count_player1}        {self.score_count_player2}",
                   align="center", font=("Verdana", 25, "normal"))



