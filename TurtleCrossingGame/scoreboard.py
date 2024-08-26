from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level:{self.score}", font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def reset_score(self):
        self.score = 0
        self.write_score()

    def signal_end(self):
        game_over = Turtle()
        screen = Screen()
        screen.bgcolor("red")
        game_over.color("black")
        game_over.penup()
        game_over.goto(-80,0)
        game_over.write("GAME OVER", font=FONT)
