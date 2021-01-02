import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
loop_iter = 5
level = 0

while game_is_on:
    if level == 0:
        carManager.generate_cars()
        level = 1

    time.sleep(0.1)
    carManager.move_all_cars(level)

    # Check for game over - collion with car
    for car in carManager.carList:
        if player.distance(car) < 20:
            screen.bye()
    # Check for game over - reached finished line
    if player.has_finished():
        # reset turtle
        player.move_to_start_pos()

        # increment level
        level += 1

    screen.update()

    loop_iter += 1
    if loop_iter == 6:
        carManager.create_car()
        loop_iter = 0
