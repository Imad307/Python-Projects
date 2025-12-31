from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.color("white")
        self.goto(0,0)
        self.dx = 1
        self.dy = 1
    def move_ball(self):
        new_x = self.xcor()+self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()