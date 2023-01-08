from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.setup_snake()
        self.head = self.snake[0]

    def setup_snake(self):
        for i in STARTING_POSITIONS:
            self.add_body(i)

    def add_body(self,i):
        snakebody = Turtle()
        snakebody.color('white')
        snakebody.shape('square')
        snakebody.penup()
        snakebody.goto(i)
        self.snake.append(snakebody)

    def extend(self):
        self.add_body(self.snake[-1].position())


    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
