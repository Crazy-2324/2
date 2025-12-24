from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("Black")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()
    if  snake.head.xcor() < -370 or snake.head.xcor() > 370 or snake.head.ycor() > 300 or snake.head.ycor() < -300 :
        game_on = False
        score.over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.over()



screen.exitonclick()