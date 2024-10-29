from turtle import Screen, Turtle
import time

x = -20
y = 0
RIGHT = 0
LEFT = 180 
UP = 90
DOWN = 270

class Snake() :
    def __init__(self) :
        self.segments = []
        self.x = x 
        self.y = y
        self.create_snake()
        self.head = self.segments[-1]
    
    def create_snake(self) :
        for position in range(3) :
            new = self.add_snake()
            new.goto(self.x, self.y)
            self.x += 20
            self.segments.append(new)
    
    def add_snake(self) :
            new = Turtle(shape="square")
            new.penup()
            new.color("green")
            return new       
    
    def extend(self) :
        new = self.add_snake()
        new.goto(self.segments[0].position())
        self.segments.insert(0, new)
        
  
               
    
    def move(self) :
        for seg in range(len(self.segments)-1) :
            new_x = self.segments[seg+1].xcor()
            new_y = self.segments[seg+1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20) 
    
    def up(self) :
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    
    def down(self) :
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
          
    def right(self) :
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)          
    
    def left(self) :
        if self.head.heading() !=  RIGHT :
            self.head.setheading(LEFT)  