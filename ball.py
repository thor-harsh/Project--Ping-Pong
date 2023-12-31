import random
from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.move_speed=0.1

        self.x_move=10
        self.y_move=10

    def go_to(self):
        self.penup()
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9
    def funtion(self):
        self.goto(0,0)
        self.move_speed=0.08
        self.bounce_x()

