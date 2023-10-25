from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        

    def create_paddles_right(self, start):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(start)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def create_paddles_left(self, start):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(start)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_paddles(self):
        pass
