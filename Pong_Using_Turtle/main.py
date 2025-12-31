# We are creating Pong!
import turtle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard, Separation
from Paddle import Paddle
import time
X_PADDLE_POSITION = 350
Y_PADDLE_POSITION = 0
my_screen = Screen()
my_screen.screensize(canvwidth=800, canvheight=600, bg="black")
my_screen.title("Pong:Arcade Games")
my_screen.tracer(0)
game_ball = Ball()
l_paddle = Paddle(X_PADDLE_POSITION, Y_PADDLE_POSITION)
r_paddle = Paddle(-X_PADDLE_POSITION, Y_PADDLE_POSITION)
player = Scoreboard()
dot_line = Separation(0, X_PADDLE_POSITION+30)
dot_line.setheading(270)
for i in range(37):
    if i%2 == 0:
        dot_line.pendown()
        dot_line.forward(17)
    else:
        dot_line.penup()
        dot_line.forward(20)
border_line = Separation(-395, 290)
border_line.pendown()
my_angle= 360
for i in range(4):
    if i%2 == 0:
        border_line.setheading(my_angle)
        border_line.forward(795)
    else:
        border_line.setheading(my_angle)
        border_line.forward(595)
    my_angle-= 90

def stop_game():
    global game_is_on
    game_is_on = False

def start_game():
    global game_is_on
    game_is_on = True

my_screen.listen()
my_screen.onkey(l_paddle.move_paddle_up, "w")
my_screen.onkey(l_paddle.move_paddle_down, "s")
my_screen.onkey(r_paddle.move_paddle_up, "Up")
my_screen.onkey(r_paddle.move_paddle_down, "Down")
my_screen.onkey(stop_game, "c")
my_screen.onkey(start_game, "p")
game_is_on = True
while game_is_on:
    time.sleep(0.00001)
    my_screen.update()
    #moving the ball
    game_ball.move_ball()
    #checking if the ball touches the sides of the pong(x-axis on pong and y-axis for ball)
    if game_ball.ycor()>290 or game_ball.ycor()<-290:
        game_ball.bounce_y()
    # checking if the ball touches the paddles
    if l_paddle.distance(game_ball)<50 and game_ball.xcor()>345 or r_paddle.distance(game_ball)<50 and game_ball.xcor()<-345:
        game_ball.bounce_x()
    # checking if the ball touches the sides of the pong(y-axis on pong and x-axis for ball)
    if game_ball.xcor()>390:
        player.score_l+=1
        game_ball.reset_pos()
    if game_ball.xcor()<-390:
        player.score_r+=1
        game_ball.reset_pos()

    player.update_score()

turtle.done()
