from turtle import Turtle


class Score(Turtle):
    def __init__(self, POSITION):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.points = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.points}", font=("Arial", 30, "normal"))

    def update_score(self):
        self.points += 1
        self.write_score()


