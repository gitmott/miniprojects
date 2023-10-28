from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        
    def create_turtle(self):
        self.shape("turtle")
        self.color("black")
        # self.heading(270)
        self.penup()
        self.setheading(90)

    def refresh_turtle(self):
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)    
