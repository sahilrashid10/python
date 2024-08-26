import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("salmon")
screen.tracer(0)

# todo 1: create a player
player = Player()
# todo 3-a generate cars
CARS = CarManager()

# score

score = Scoreboard()
# todo 2: control turtle by up key
screen.listen()
screen.onkey(player.move, "space")

flag = True
t = 0.1
while flag:
    time.sleep(t)
    # todo 3-b generate randomly positioned cars
    CARS.generate_car()
    # todo 4. make em move right to left
    CARS.move_cars()
    screen.update()

    #todo 4 a-Detect collision with roof
    #todo 4 b-increase the speed of cars
    #todo 4 c-increase score
    if player.ycor() > 280:
        t = player.collision_roof(t)
        score.update_score()

    #todo 5 a-check for collision with cars
    #todo 5-b reset score and turtle
    for car in CARS.car_list:
        if player.distance(car) < 30:
            t = player.collision_car(t)
            score.reset_score()
            flag = False
            score.signal_end()

screen.exitonclick()

