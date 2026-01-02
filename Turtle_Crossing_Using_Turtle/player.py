from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset_turtle()

    def move_turtle_ahead(self):
        self.forward(MOVE_DISTANCE)

    def move_turtle_backward(self):
        self.backward(MOVE_DISTANCE)

    def move_turtle_left(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        x_cor -= MOVE_DISTANCE
        self.goto(x_cor, y_cor)
    def move_turtle_right(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        x_cor+= MOVE_DISTANCE
        self.goto(x_cor, y_cor)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

