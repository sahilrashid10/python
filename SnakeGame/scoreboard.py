from turtle import Turtle

FONT = ('Arial', 20, 'normal')
ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self, turtle_name):
        super().__init__()
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", FONT)

    def update_score(self):
        self.write(f"score = {self.score}", False, ALIGN, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()