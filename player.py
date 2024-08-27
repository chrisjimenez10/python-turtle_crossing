from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.teleport(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
        self.penup()

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def next_round(self):
        self.goto(STARTING_POSITION)
