from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scorecard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

my_snake = Snake()
food = Food()
game_score = Scorecard()

screen.listen()
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    
    # detect collision
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        game_score.increase_score()

    # detect collision with wall
    if my_snake.head.xcor()>280 or my_snake.head.xcor()<-280 or my_snake.head.ycor()>280 or my_snake.head.ycor()<-280:
        # game_is_on = False
        # game_score.game_over()
        game_score.reset()
        my_snake.reset()

    # detect collision with tail
    for segment in my_snake.segments:
        if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) <10:
            # game_is_on = False
            # game_score.game_over()  
            game_score.reset()
            my_snake.reset()



screen.exitonclick()