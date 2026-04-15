from random import randint
from turtle import Turtle,Screen
import random

from replit import clear


# def move_forwards():
#     tim.forward(10)
# def move_backward():
#     tim.back(10)
# def move_right():
#     tim.right(10)
# def move_left():
#     tim.left(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# sc.listen()
# sc.onkey(key="w",fun=move_forwards)
# sc.onkey(key="s",fun=move_backward)
# sc.onkey(key="d",fun=move_right)
# sc.onkey(key="a",fun=move_left)
# sc.onkey(key="c",fun=clear)
#*****************************************************************

sc=Screen()
sc.setup(500,400)
pace=random.randint(0,30)
is_race_on = False
user_bet=sc.textinput(title="Make Your Bet.",prompt="which turtle will win the race?Enter The Colour")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x=-230
y=-100
all_turtles = []
for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x,y)
    y=y+40
    tim.color(colors[turtle_index])
    all_turtles.append(tim)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

sc.exitonclick()
