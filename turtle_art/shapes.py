from turtle import Turtle, Screen

tt = Turtle()
tt.shape("turtle")
tt.color("DarkViolet")
tt.pen(fillcolor="DarkViolet", pencolor="black")
tt.pensize(5)

sides = 3
while sides <= 10:
    for side in range(sides):
        tt.pd()
        tt.fd(100)
        tt.right(360/sides)
    sides += 1

screen = Screen()
screen.exitonclick()