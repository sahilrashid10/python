from turtle import Turtle
import random

COLORS = ["orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []

    def generate_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)
