import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_objects = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        car_gen = random.randint(1, 6)
        if car_gen == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(280, random.randint(-240, 240))
            self.car_objects.append(car)

    def move_cars(self):
        for obj in self.car_objects:
            obj.forward(self.car_speed)

    def carspeed(self):
        self.car_speed += MOVE_INCREMENT

