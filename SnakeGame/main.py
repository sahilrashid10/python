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
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


snake.create_snake()

while True:
    time.sleep(0.05)
    screen.update()
    snake.move()
    #detecting collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # detecting collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.write_score()
        screen.bgcolor("red")
        time.sleep(1)
        screen.bgcolor("white")
        snake.reset()

    #detecting collision with the tail(i.e : if head collides with any od the segment)
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.write_score()
            screen.bgcolor("red")
            time.sleep(1)
            screen.bgcolor("white")
            snake.reset()
