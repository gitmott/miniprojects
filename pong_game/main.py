from turtle import Screen, Turtle
from paddles import Paddle

screen = Screen()
paddle = Paddle()

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)



screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

paddle.create_paddles_right((350, 0))
# paddle.create_paddles_left((-350, 0))

screen.exitonclick()