import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)

# # square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# drawing shapes
# def draw_shapes(number_of_sides):
#     angle =360/number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# for shape_side in  range(3,11):
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side)

# random walk
# def rand_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
# tim.pensize(10)
# # colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.speed(10)
# direction = [0,90,180,270]

# for _ in range(200):
#     tim.color(rand_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(20)

# draw a spirograh
# def rand_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
# tim.speed(0)

# def draw_spirograph(steps):
#     for _ in range(int(360/steps)):
#         tim.color(rand_color())
#         tim.left(steps)
#         tim.circle(100)

# draw_spirograph(10)



screen = t.Screen()
screen.exitonclick()