from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as f:
            content = f.read()
            if content == "":
                self.highscore = 0
            else:
                self.highscore = int(content)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align="center", font=("Arial", 20, "bold"))

    def score_increase(self):
        self.score += 1
        self.update_score()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("Game Over!!", align="center", font=("Arial", 20, "bold"))
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        with open("score.txt",mode="w") as data:
            data.write(f"{self.highscore}")
        self.score=0
        self.update_score()