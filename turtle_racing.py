import random
from turtle import Turtle, Screen
#set up the screen
screen = Screen()
screen.setup(height=400, width=500)
# take a bet from user
user_bet = screen.textinput("Who will Win", "Entre a color: ").lower()
colors = ["red", "blue", "orange", "green", "yellow", "yellow4", "RosyBrown2"]
y_index = [ -90, -50, -10, 30, 70, 110, 150]
turtles = []
#create a flag so that you make sure that if user has entered a bet then race starts
flag = False
#create 5 turtles
for turtle_no in range(7):
    turtle_name = Turtle("turtle")
    turtle_name.color(colors[turtle_no])
    turtle_name.penup()
    turtle_name.goto(-230, y_index[turtle_no])
    turtles.append(turtle_name)

if user_bet:
    flag = True

while flag:
    for t in turtles:
        random_steps = random.randint(0,20)
        t.forward(random_steps)
        if t.xcor() > 227:
            print(f"{t.pencolor()}: WON")
            if t.pencolor() == user_bet:
                print("YOU WIN 😍")
            else:
                print("YOU LOSE 🧟‍♂️")
            flag = False


screen.exitonclick()
