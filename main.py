from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "m")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scoreCount()
    if snake.detectwallCollision():
        score.gameover()
        break

    # detect collision with own tail
    for x in snake.segments[1:]:
        if snake.head.distance(x) < 10 :
            score.gameover()
            break




screen.exitonclick()