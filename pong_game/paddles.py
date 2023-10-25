from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        

    def create_paddle(self, start):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(start)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
