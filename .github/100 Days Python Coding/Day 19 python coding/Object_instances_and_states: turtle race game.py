import turtle
from turtle import Turtle, Screen
import random

# Object instance and state: Python turtle coordinates
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet now", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle= []

def create_turtle(rbg, x_axis, y_axis):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rbg)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    all_turtle.append(new_turtle)

x = -230
y = -120

if user_input:
    is_race_on = True

for color in colors:
    y += 40
    create_turtle(color, x, y)
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()