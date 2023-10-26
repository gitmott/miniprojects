from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
import time

screen = Screen()
r_paddle = Paddle()
l_paddle = Paddle()
ball = Ball()



screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

r_paddle.create_paddle((350, 0))
l_paddle.create_paddle((-350, 0))
# paddle.create_paddles_left((-350, 0))

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >=290 or ball.ycor() <= -290:
        ball.bounce()

    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.hit_paddle()
    elif ball.xcor() > 380:
        print("Point L") ## Needs to add score to L
        ball.reset_position()
    elif ball.xcor() < -390:
        print("point R") ## Needs to add score to R
        ball.reset_position()

    


screen.exitonclick()