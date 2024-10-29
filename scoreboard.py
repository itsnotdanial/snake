from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        
    def game_over(self) :
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
              
    def update_score(self) :
        self.score += 1
        self.hideturtle()
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
          
        
        