from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("white")

snake = Snake()
food = Food()
scoreboard = ScoreBoard(snake)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.bgpic()

snake.create_snake()

flag = True
while flag:
    time.sleep(0.08)
    screen.update()
    snake.move()
    #detecting collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # detecting collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        flag = False

    #detecting collision with the tail(i.e : if head collides with any od the segment)
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            flag = False

screen.exitonclick()
