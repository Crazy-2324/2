from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]
    def create_snake(self):
        for position in  STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        newsegment = Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for s_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[s_num - 1].xcor()
            new_y = self.segments[s_num -1].ycor()
            self.segments[s_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)