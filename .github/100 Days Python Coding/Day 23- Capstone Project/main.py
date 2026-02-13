from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Score

player = Player()
car_manager = CarManager()
score = Score()

screen = Screen()
screen.title("Crossing Turtle Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.listen()
screen.onkey(fun=player.move_up, key="Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    # move cars across screen
    car_manager.create_cars()
    car_manager.move()
    # detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_on = False
            score.game_over()

    # detect if player gets to finish line
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.change_level()
        score.increase_level()



screen.exitonclick()