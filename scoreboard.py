from turtle import Turtle

FONT = ("Courier", 24, "bold")
FONT_SCORE = ("Courier", 12, "bold")
ALIGNMENT = "center"
SCORE_ALIGNMENT = (-290, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_ALIGNMENT)
        self.update_score()

    def game_over(self):
        self.home()
        self.write(arg="🤣 GAME OVER...", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update_score()


    def update_score(self):
        self.write(arg=F"Level: {self.current_level}", font=FONT_SCORE)
