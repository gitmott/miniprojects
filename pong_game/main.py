from turtle import Screen, Turtle
from paddles import Paddle

screen = Screen()
paddle = Paddle()


screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")

paddle.create_paddles_right((350, 0))
# paddle.create_paddles_left((-350, 0))

screen.exitonclick()