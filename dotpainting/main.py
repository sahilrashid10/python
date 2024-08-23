import random
from locale import currency

import colorgram
import turtle

tim = turtle.Turtle()
tim.hideturtle()


rgb_colors = []
colors = colorgram.extract("color.jpg", 20)
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, b, g)
    rgb_colors.append(new_color)
tim.speed("fastest")
tim.penup()
colors_list = [(187, 94, 42), (244, 36, 149), (237, 39, 73), (210, 135, 66), (219, 19, 58), (238, 63, 215), (52, 189, 76), (173, 52, 21), (87, 210, 89), (40, 165, 46), (212, 18, 152), (226, 207, 104), (83, 229, 153), (192, 15, 22), (99, 29, 182), (57, 194, 145), (200, 43, 208), (0, 123, 45), (225, 249, 139), (96, 110, 5)]
turtle.colormode(255)
tim.setheading(220)
tim.forward(290)
tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
