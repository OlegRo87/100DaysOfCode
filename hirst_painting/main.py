# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
import turtle as turtle_mode
import random


turtle_mode.colormode(255)
tim = turtle_mode.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_mode.Screen()
screen.exitonclick()