from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE= 20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head =self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg -1].xcor()
            new_y=self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]

    def left(self):
        self.head.left(90)
        # self.move()

    def right(self):
        self.head.right(90)
        # self.move()