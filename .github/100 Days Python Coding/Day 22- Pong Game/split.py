from turtle import Turtle

class Split(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line()

    def draw_line(self):
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)