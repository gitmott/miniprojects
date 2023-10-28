import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")

player.create_turtle()
player.refresh_turtle()

scoreboard.update_scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > -120:
        player.refresh_turtle()
        scoreboard.update_scoreboard()



screen.exitonclick()


# TODO Fix scoeboard
# TODO create scoring when turtle gets to end (y=200??)
# TODO refresh when turtle gets to end
# TODO add score when turtle gets to end
# TODO create cars
# TODO increase car speed when turtle reaches end
# TODO create car collision, gameover condition
