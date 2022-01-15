from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 23, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=280)
        self.update_score()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.highScore}")
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highScore}", move=False, align=ALIGNMENT, font=FONT)
