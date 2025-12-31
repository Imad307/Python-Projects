from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.hideturtle()
        self.goto(0,350)

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score_l}  {self.score_r}", align="center", move=False, font=("Arial", 20, "bold"))

class Separation(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x,y)
