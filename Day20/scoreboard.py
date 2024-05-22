from turtle import Turtle
# constants
ALIGNMENT = "center"
FONT = ("Arial",24, "normal")

class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("C:/Users/stejaram/Downloads/100daysofPython/Day20/data.txt") as file:
            self.high_score = file.read()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1        
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score=self.score
            with open("C:/Users/stejaram/Downloads/100daysofPython/Day20/data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    