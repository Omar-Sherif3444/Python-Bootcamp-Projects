from turtle import Screen,Turtle
from Snake import  Snake
from Food import Food
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()
sc=Screen()
sc.setup(600,600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)
score=0

snake=Snake()
food = Food()
sc.listen()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.right,"Right")
sc.onkey(snake.left,"Left")

game_is_on=True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <15:
        food.randommove()
        snake.extend()
        scoreboard.score_increase()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.gameover()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()
sc.exitonclick()
