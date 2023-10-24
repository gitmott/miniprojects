from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    

    snake.move()

    if snake.head.distance(food) < 15:
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        # new_seg.goto(position)
        snake.segments.append(new_seg)
        food.refresh()
        scoreboard.increase_score()




screen.exitonclick()