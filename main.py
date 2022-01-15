import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Turtle Eater Snake")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    '''Food Eaten'''
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    '''wall collision'''
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() < -310 or snake.head.ycor() > 320:
        score.reset()
        snake.reset()

    '''self bite'''
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()

screen.exitonclick()
