from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball

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
    screen.update()
    # ball.move()

screen.exitonclick()