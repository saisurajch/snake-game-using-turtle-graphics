from turtle import Turtle


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.write(f"Game Over!", align="center", font=("Courier", 30, "normal"))
