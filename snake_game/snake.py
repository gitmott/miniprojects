from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

screen = Screen

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):     
        for position in STARTING_POSITION:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move(self):
        for seg in range(len(self.segments) -1, 0,-1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)