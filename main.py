import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")

player = Player()
# make player go up
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.ycor() > 280:  # 280 is the finish line
        player.goto(0, -280)  # return to the start position
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
