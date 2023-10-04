from turtle import Turtle, Screen


def row():
    for step in range(18):
        colour = random.choice(possible_colours)
        tt.pen(pencolor=colour)
        tt.pendown()
        tt.fd(1)
        tt.penup()
        tt.fd(50)


possible_colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen"
                    , "green", "darkgreen", "chocolate", "brown", "black", "gray"]
tt = Turtle()
tt.shape("turtle")
tt.color("DarkViolet")
tt.pensize(20)
tt.speed(0)
x = -450
y = -380

tt.setx(x)
tt.sety(y)
tt.penup()
number_rows = 0

while number_rows < 16:
    row()
    tt.setx(x)
    y += 50
    tt.sety(y)
    number_rows += 1


# for step in range(number_steps):
#     colour = random.choice(possible_colours)
#     direction = random.choice(possible_directions)
#     tt.pen( pencolor=colour)
#     tt.rt(direction)


screen = Screen()
screen.exitonclick()