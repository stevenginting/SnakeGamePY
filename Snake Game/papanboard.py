from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
STRIKE_FONT = ("Courier", 36, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        if self.score > 3:
            self.goto(0, 230)
            self.color("yellow")
            self.write("STRIKE", align=ALIGNMENT, font=STRIKE_FONT)
            self.color("white")
            self.goto(0, 270)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()