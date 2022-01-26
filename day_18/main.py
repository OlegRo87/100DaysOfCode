import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)


# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


#
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)


tim.speed("fastest")


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shade_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shade_side_n)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
