#importing modules
import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#setuping screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#creating necessary objects
my_turtle = Player()
score = Scoreboard()
car = CarManager()
#setting up the key listening
screen.listen()
screen.onkey(my_turtle.move_turtle_ahead, "Up")
screen.onkey(my_turtle.move_turtle_backward, "Down")
screen.onkey(my_turtle.move_turtle_left, "Left")
screen.onkey(my_turtle.move_turtle_right, "Right")
#main game logic
game_is_on = True
while game_is_on:
    time.sleep(0.1) #time for refreshing the screen/logic
    screen.update()# updating the screen
    car.create_car()#creating new cars
    car.move_cars()#moving cars at a speed
    for car_obj in car.car_objects: # loop to check collision 
        if my_turtle.distance(car_obj)<25:
            score.game_over()
            game_is_on = False
        if car_obj.xcor()<-290:
            car_obj.hideturtle()
            car.car_objects.remove(car_obj)
    if my_turtle.ycor()>290:#checking the turtle's level
        my_turtle.reset_turtle()
        score.update_level()
        car.carspeed()
turtle.done()
