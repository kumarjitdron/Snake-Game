from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font =("Arial", 24, "normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font =("Arial", 24, "normal"))


    def scoreCount(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))





