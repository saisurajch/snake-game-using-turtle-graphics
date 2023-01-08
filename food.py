import random
from turtle import Turtle
COLORS = ['yellow','blue']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(COLORS))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x,y)
