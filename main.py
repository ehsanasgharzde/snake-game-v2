from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# from border import Border
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game!')
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# border = Border()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


gameon = True

while gameon:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoretrack()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()