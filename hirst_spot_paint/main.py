# import colorgram
import random
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(250)
# tim.pendown()
tim.setheading(0)
x_corr = tim.xcor()
y_corr = tim.ycor()
color_list = [(238, 240, 245), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]
for _ in range(10):
    for _ in range(10):
        tim.dot(10, random.choice(color_list))
        # tim.penup()
        tim.forward(30)
        # tim.pendown()
    y_corr += 30
    # tim.penup()
    tim.sety(y_corr)
    tim.setx(x_corr)
    # tim.pendown()


screen = t.Screen()
screen.exitonclick()
