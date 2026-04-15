from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time
sc = Screen()
sb=Scoreboard()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Pong")
sc.tracer(0)

p1 = Paddle(x_cor=380,y_cor=0)
p2=Paddle(x_cor=-380,y_cor=0)
ball=Ball()
sc.listen()
sc.onkey(p1.go_up, "Up")
sc.onkey(p1.go_down, "Down")
sc.onkey(p2.go_up, "w")
sc.onkey(p2.go_down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()
    sc.update()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(p1)<50 and ball.xcor()>340 and ball.x_move > 0 :
        ball.bbounce()
    if ball.distance(p2) < 50 and ball.xcor() < -340 and ball.x_move< 0 :
        ball.bbounce()
    if ball.xcor()>350 :
        sb.l_point()
        ball.goto(0,0)
        ball.x_move *= -1
    if ball.xcor()<-350:
        sb.r_point()
        ball.goto(0,0)
        ball.x_move *= -1





sc.exitonclick()