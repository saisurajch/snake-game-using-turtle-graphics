from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from gameover import GameOver
import time

# initializing
screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
gameover = GameOver()

# setting up screen
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Writing the game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Food collision trigger
    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        snake.extend()
        food.refresh()
    # Detecting wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameover.game_over()
        is_game_on = False
    # Detecting tail collision
    for snakebody in snake.snake:
        if snakebody == snake.head:
            pass
        elif snake.head.distance(snakebody) < 10:
            gameover.game_over()
            is_game_on = False

screen.exitonclick()
