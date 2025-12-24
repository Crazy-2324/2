from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.rewrite()
    def rewrite(self):
        self.write(f"SCORE : {self.score}",align="center",font=("arial",24,"normal"))
    def over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("arial",24,"normal"))

    def update(self):
        self.score+= 1
        self.clear()
        self.rewrite()
