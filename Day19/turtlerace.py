from turtle import Turtle, Screen
import random
# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# tit = Turtle(shape="turtle")
# tat= Turtle(shape="turtle")

# tim.color("red")
# tom.color("green")
# tit.color("yellow")
# tat.color("purple")

# def start_pos():
#     tim.goto(x=-240,y=-150)
#     tom.goto(x=-240,y=-100)
#     tit.goto(x=-240,y=100)
#     tat.goto(x=-240,y=150)

is_race_on= False
screen = Screen()
screen.setup(width=500, height=400)
# start_pos()
user_bet=screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colors = ["red","yellow","green","blue","orange","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on= False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"you've won! The {winning_color} turtle is the winner")
            else:
                print(f"you've lost! The {winning_color} turtle is the winner")
        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)


screen.listen()

screen.exitonclick()