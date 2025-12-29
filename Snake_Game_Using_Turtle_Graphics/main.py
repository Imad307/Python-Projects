from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

my_snake = Snake()

snake_food = Food()
snake_score = Scoreboard()

my_screen.listen()

my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

snake_is_alive = True

while snake_is_alive:
    my_screen.update()
    time.sleep(0.15)
    my_snake.move()
    #Detect collision with Food
    if my_snake.head.distance(snake_food)<15:
        snake_food.refresh()
        snake_score.score_increase()
        my_snake.extend_snake()

    # Detect collision with Wall
    if my_snake.head.xcor() > 290 or my_snake.head.ycor() > 290 or my_snake.head.xcor()<-290 or my_snake.head.ycor() < -290:
        snake_is_alive = False
        snake_score.game_over()

    for pos in my_snake.snake_pos[1:]:
        if my_snake.head.distance(pos)<10:
            snake_is_alive = False
            snake_score.game_over()
    '''Why the below one didn't work? 
    Because, the turtle position returns the tuple and I am comparing a tuple(x,y) against turtle objects
    which will never be true.'''
    # if my_snake.head.position() in my_snake.snake_pos[1:]: #
    #     snake_is_alive = False
    #     snake_score.game_over()
my_screen.mainloop()
