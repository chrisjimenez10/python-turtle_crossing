from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def game_over(self):
        self.home()
        self.write(arg="🤣 GAME OVER...", align=ALIGNMENT, font=FONT)

