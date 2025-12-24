from turtle import Turtle
positions = [(-370,300),(-370,-300),(370,-300),(370,300),(-370,300)]
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.edge()
    

    def edge(self):
        for x in positions:
                self.goto(x)
                self.pendown()