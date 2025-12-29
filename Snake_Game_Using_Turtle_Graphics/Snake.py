from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
class Snake:
    def __init__(self):
        self.snake_pos = []
        self.create_snake()
        self.head = self.snake_pos[0]
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)
    def add_segment(self, pos):
        my_snake = Turtle("square")
        my_snake.color("green")
        my_snake.penup()
        my_snake.goto(pos)
        self.snake_pos.append(my_snake)
    def move(self):
        for snake_ind_positions in range(len(self.snake_pos)-1, 0, -1):
            new_x = self.snake_pos[snake_ind_positions-1].xcor()
            new_y = self.snake_pos[snake_ind_positions - 1].ycor()
            self.snake_pos[snake_ind_positions].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def extend_snake(self):
        self.add_segment(self.snake_pos[-1].position())

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
