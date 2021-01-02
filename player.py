from turtle import Turtle

STARTING_COORDS = {"X": 0, "Y": -200}
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.move_to_start_pos()
        self.setheading(UP)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def has_finished(self):
        return self.ycor() >= FINISH_LINE_Y

    def move_to_start_pos(self):
        self.goto(x=STARTING_COORDS["X"], y=STARTING_COORDS["Y"])
