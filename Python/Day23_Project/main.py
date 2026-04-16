import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

sb = Scoreboard()
p = Player()
c = CarManager()
game_is_on = True
screen.listen()
screen.onkey(p.move_up,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    r=random.randint(1,6)
    if r<=2:
        c.create_car()
    c.move_cars()
    for car in c.cars:
        if car.distance(p)<20:
            sb.game_over()
            game_is_on=False
    if p.ycor()>=200:
        p.goto(0,-280)
        c.inc()
        sb.level_up()
screen.exitonclick()