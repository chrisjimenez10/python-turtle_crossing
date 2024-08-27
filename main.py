import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(fun=player.move, key="Up")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False


    # Successfull player crossing: Reset player position for next round
    if player.ycor() >= 280:
        player.next_round()
        car_manager.level_up()
        score_board.increase_level()


screen.exitonclick()
