from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.speed(0)

def move_forwards():
    t.fd(10)


def move_backwards():
    t.bk(10)


def turn_left():
    t.left(10)
    

def turn_right():
    t.right(10)


def clear():
    t.clear()
    t.reset()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)



screen.exitonclick()
