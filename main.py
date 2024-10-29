from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

draco = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(draco.up, "Up")
screen.onkey(draco.down, "Down")
screen.onkey(draco.right, "Right")
screen.onkey(draco.left, "Left")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    draco.move()
    if draco.head.distance(food) < 15 :
        food.refresh()
        draco.extend()
        score.update_score()
    
    if draco.head.xcor() > 280 or draco.head.xcor() < -295 or draco.head.ycor() > 280 or draco.head.ycor() < -280 :
        game_is_on = False
        score.game_over()
    
    for seg in draco.segments :
        if seg == draco.head :
            pass
        
        elif draco.head.distance(seg) < 10 :
            score.game_over()
            game_is_on = False
               
             
    




        
        
           
    
    















screen.exitonclick()