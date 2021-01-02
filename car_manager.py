from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_COORDS = {"X": 300, "Y": 0}
WIDTH = 2
HEIGHT = 1
LEFT = 180
STARTING_NUM_CARS = 10


class CarManager:
    def __init__(self):
        self.carList = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.speed("fastest")
        new_car.color(COLORS[randint(0, 5)])
        new_car.shapesize(stretch_len=WIDTH, stretch_wid=HEIGHT)
        y_pos = self.get_y_coord()
        x_pos = self.get_x_coord()
        new_car.goto(x=x_pos, y=y_pos)
        new_car.setheading(LEFT)
        self.carList.append(new_car)

    def move_all_cars(self, level):
        move_distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1)
        for car in self.carList:
            car.forward(move_distance)

    def get_y_coord(self):
        return randint(-8, 8) * 20

    def get_x_coord(self):
        return STARTING_COORDS["X"] + randint(0, 15) * 10

    def destroy_car(self, carIndex):
        self.carList.pop(carIndex)

    def generate_cars(self):
        for _ in range(STARTING_NUM_CARS):
            self.create_car()