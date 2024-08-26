from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def collision_roof(self, sec):
        sec -= 0.03
        self.goto(STARTING_POSITION)
        return sec

    def collision_car(self, sece):
        sec = 0.1
        self.goto(STARTING_POSITION)
        return sec




