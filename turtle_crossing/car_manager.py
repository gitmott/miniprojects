from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WIDTH = 40
LENGTH = 20




class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.width(WIDTH)
        self.color(random.choice(COLORS))

    def make_car(self):
        pass

