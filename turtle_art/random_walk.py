from turtle import Turtle, Screen
import random

tt = Turtle()
tt.shape("turtle")
tt.color("DarkViolet")
tt.pen(fillcolor="DarkViolet", pencolor="black")
tt.pensize(5)

possible_directions = [90, 180, 270, 0]
possible_colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen"
                    , "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
number_steps = random.choice(range(1, 101))
print(number_steps)

for step in range(number_steps):
    colour = random.choice(possible_colours)
    direction = random.choice(possible_directions)
    tt.pen( pencolor=colour)
    tt.fd(30)
    tt.rt(direction)


screen = Screen()
screen.exitonclick()