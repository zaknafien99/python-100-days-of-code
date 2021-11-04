from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} High Score: {self.high_score}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        if self.level > self.high_score:
            self.high_score = self.level
        self.level = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=FONT)
