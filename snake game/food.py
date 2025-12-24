from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.color("red")
    def refresh(self):
        r_x= random.randint(-280,280)
        r_y = random.randint(-280,280)
        self.goto(r_x,r_y)