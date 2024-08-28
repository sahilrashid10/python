from idlelib.browser import file_open
from turtle import Turtle

FONT = ('Arial', 10, 'normal')
ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-30, 260)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def write_score(self):
        if self.score > self.high_score:
            with open("data.txt",'w') as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, "center", FONT)

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score}, HIGH SCORE {self.high_score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
