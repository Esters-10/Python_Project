from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
from split import Split

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
split = Split()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")
screen.tracer(0)



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect if ball goes out of bound r_paddle
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # detect if ball goes out of bound l_paddle
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()
