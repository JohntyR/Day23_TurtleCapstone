from turtle import Turtle

ALIGNMENT = "center"
FONT = "Tahoma"
FONT_SIZE = 16
FONT_WEIGHT = "normal"
FONT_COLOUR = "black"
X_POS = -250
Y_POS = 270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color(FONT_COLOUR)
        self.penup()
        self.goto(x=X_POS, y=Y_POS)
        self.hideturtle()
        self.refresh()

    def increment_level(self):
        self.level += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(
            f"Level: {self.level}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_WEIGHT)
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_WEIGHT))
