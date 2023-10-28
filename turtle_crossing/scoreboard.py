from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.level += 1


