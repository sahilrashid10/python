from time import sleep
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.new_x = 1
        self.new_y = 1

    def move(self):
        self.penup()
        y = self.ycor() + self.new_y
        x = self.xcor() + self.new_x
        self.goto((x, y))

    def collision_walls(self):
        self.new_y *= -1
        self.move()

    def collision_paddle(self, delay):
        self.new_x *= -1
        self.move()
        delay -= 0.002
        return delay

    def restart(self, delay):
        self.new_x *= -1
        self.new_y *= -1
        delay = 0.01
        self.goto((0, 0))
        self.move()
        return delay
