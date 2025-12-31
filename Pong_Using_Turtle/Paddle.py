from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.speed(0)
        self.color("white")
        self.goto(x,y)
        self.dy = 20

    def move_paddle_up(self):
        if self.ycor()<290:
            self.sety(self.ycor()+self.dy)

    def move_paddle_down(self):
        if self.ycor() > -290:
            self.sety(self.ycor()-self.dy)




