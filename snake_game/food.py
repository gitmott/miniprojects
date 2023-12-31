from turtle import Turtle 
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(randomx, randomy)

    def refresh(self):
        random_x_food = random.randint(-280, 280)
        random_y_food = random.randint(-280, 280)
        self.goto(random_x_food, random_y_food)




