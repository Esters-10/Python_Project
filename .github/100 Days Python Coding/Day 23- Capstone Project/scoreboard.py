from turtle import Turtle

FONT = ("courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.view_level()

    def view_level(self):
        self.hideturtle()
        self.penup()
        self.setposition(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.view_level()


