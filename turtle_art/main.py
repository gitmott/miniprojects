from turtle import Turtle, Screen

tt = Turtle()
tt.shape("turtle")
tt.color("DarkViolet")
tt.pen(fillcolor="DarkViolet", pencolor="black")
tt.pensize(5)


# triangle
for side in range(3):
    tt.pd()
    tt.fd(100)
    tt.right(120)

# square
for side in range(4):
    tt.pd()
    tt.fd(100)
    tt.right(90)    
# pent
for side in range(5):
    tt.pd()
    tt.fd(100)
    tt.right(360/5)    
# hex
for side in range(6):
    tt.pd()
    tt.fd(100)
    tt.right(360/6)    
# sev
for side in range(7):
    tt.pd()
    tt.fd(100)
    tt.right(360/7)    
# oct
for side in range(8):
    tt.pd()
    tt.fd(100)
    tt.right(360/8)    


















screen = Screen()
screen.exitonclick()