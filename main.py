import colorgram
colors = colorgram.extract('image.jpg', 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

# getting rid of white/background colors from our Hirst's image
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# 10x 10, dot size 20, space apart by 50
import turtle as t
import random
t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

# changing starting point to fit everything inside our drawing board
turtle.setheading(230)
turtle.forward(250)
turtle.setheading(0)


number_of_dots = 101
for dot_count in range(1,number_of_dots):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dot_count%10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

# exit on click
screen = t.Screen()
screen.exitonclick()


