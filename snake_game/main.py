from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(position)
    segments.append(new_seg)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) -1, 0,-1):
        new_x = segments[seg -1].xcor()
        new_y = segments[seg -1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].fd(20)
        
# TODO Controls for snake, it currently moves right forever



screen.exitonclick()