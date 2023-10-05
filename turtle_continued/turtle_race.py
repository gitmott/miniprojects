from turtle import Turtle, Screen


a = Turtle()
b = Turtle()
c = Turtle()
screen = Screen()
turtles = [a, b, c]
colors = ["yellow", "gold", "orange"]

y = -100
for turtle in turtles:
    turtle.sety(y)
    y +=100


    

a.fd(10)
b.fd(10)
c.fd(100)

screen.exitonclick()