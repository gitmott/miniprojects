from turtle import Screen, Turtle
from paddles import Paddle

screen = Screen()
paddle = Paddle()





screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

paddle.create_paddles_right((350, 0))
# paddle.create_paddles_left((-350, 0))

game_on = True
while game_on:
    screen.update()

screen.exitonclick()