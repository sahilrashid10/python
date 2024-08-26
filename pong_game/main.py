from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# todo 1: setup screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
#todo 1:sub - hide animation
screen.tracer(0)

# todo 2: create 2 paddles - (Note:positions are passed as tuples)
paddle_left = Paddle((-380, 0))
paddle_right = Paddle((380, 0))

#todo 4. make the paddles move
screen.listen()
screen.onkey(paddle_right.move_up, 'Left')
screen.onkey(paddle_right.move_down, 'Right')

screen.onkey(paddle_left.move_up, 'a')
screen.onkey(paddle_left.move_down, 'd')

# todo 5: create a ball
ball = Ball()

# todo 8. a- make score board work
score_right = Score((25, 250))
score_left = Score((-25, 250))

# todo 9. increase ball speed if it hits any paddle
delay = 0.01
flag = True
while flag:
    screen.update()
    time.sleep(delay)
    ball.move()
    # todo 6: a- collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_walls()

    #todo 6 b- collision with paddles
    if (ball.distance(paddle_right) < 63.2 and ball.xcor() > 370 or
            ball.distance(paddle_left) < 63.2 and ball.xcor() < -370):
        delay = ball.collision_paddle(delay)

    # todo 7 make sure if player misses a ball or not(make ball move in opp dirn)
    # todo 8. b- make score board work
    if ball.xcor() > 380:
        delay = ball.restart(delay)
        score_left.update_score()
    if ball.xcor() < -380:
        delay = ball.restart(delay)
        score_right.update_score()

screen.exitonclick()
