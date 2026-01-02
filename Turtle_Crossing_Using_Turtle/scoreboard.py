from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-290, 290)
        self.level = 0
        self.update_level()
    def update_level(self):
        self.clear()
        self.level+=1
        self.write(arg=f"Level {self.level}", move= False, align="left", font=FONT )

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"GAME OVER at Level {self.level}", move= False, align="center", font=FONT)
