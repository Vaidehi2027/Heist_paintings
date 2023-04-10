import turtle as t
from turtle import Screen
import random
t.colormode(255)
# import colorgram
# # extracts colors from images
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
# # for using in turtle want the colors in tuples of r,g and b
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r,g,b)
#     rgb_colors.append(color)
# print(rgb_colors)
color_list = [ (210, 171, 83), (22, 115, 152), (158, 30, 46),(170, 74, 51), (225, 202, 131),   (16, 27, 60),  (184, 163, 43),
 (42, 109, 80), (135, 181, 165), (7, 55, 35), (56, 21, 42), (36, 165, 189),  (13, 89, 65),
 (196, 102, 68), (9, 98, 107), (223, 171, 180), (172, 101, 112), (160, 206, 214), (225, 175, 170), (36, 64, 97)]
#draw the dots
# make a 10 by 10 pattern
# make the dot of 10 size
# move forward without printing
tim = t.Turtle()
# for starting at the end of the page we have to write some lines of code
tim.speed("fast")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if(dot_count%10==0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
