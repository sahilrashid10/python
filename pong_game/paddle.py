from time import sleep
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, POSITION):
        super().__init__()
        self.shape("square")
        self.turtlesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(POSITION)

    def move_up(self):
        Y = self.ycor()+25
        self.goto(self.xcor(), Y)

    def move_down(self):
        Y = self.ycor()-25
        self.goto(self.xcor(), Y)




