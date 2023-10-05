from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=400)
race_on = False
user_guess = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue"]
all_turtles = []


y = -200
x = -175 

for turtle_index in range(0, 9):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.sety(y)
    new_turtle.setx(x)
    y +=50
    all_turtles.append(new_turtle)


if user_guess:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print("Your turtle won!")
            else:
                print(f"You bet on the wrong turtle. The {winner} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
    



# for move in random.choice(0, 10):


screen.exitonclick()