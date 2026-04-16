COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        t=Turtle()
        t.penup()
        t.goto(300, random.randint(-280, 280))
        t.shape("square")
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.color(random.choice(COLORS))
        self.cars.append(t)
    def move_cars(self):
        for car in self.cars:
            nx=car.xcor()-self.car_speed
            car.goto(nx,car.ycor())
    def inc(self):
        self.car_speed+=MOVE_INCREMENT
