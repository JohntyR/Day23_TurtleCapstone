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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
loop_iter = 0

while game_is_on:
    if scoreboard.level == 0:
        carManager.generate_cars()
        scoreboard.increment_level()

    time.sleep(0.1)
    carManager.move_all_cars(scoreboard.level)

    # Check for game over - collion with car
    for car in carManager.carList:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Check for game over - reached finished line
    if player.has_finished():
        # reset turtle
        player.move_to_start_pos()

        # increment level
        scoreboard.increment_level()

    loop_iter += 1
    if loop_iter == 6:
        carManager.create_car()
        loop_iter = 0

    screen.update()
screen.exitonclick()