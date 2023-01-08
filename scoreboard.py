from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.score += 1
