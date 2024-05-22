import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_player = Player()
cars = CarManager()
score= Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(my_player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    # if turtle has reached finish line
    if my_player.is_at_finish_line():
        # print("you win")
        my_player.go_to_Start()
        cars.level_up()
        score.level_up()
        

    for car in cars.all_cars:
        if car.distance(my_player) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
