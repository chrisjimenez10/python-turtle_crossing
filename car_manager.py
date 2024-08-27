from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WIDTH = 1
LENGTH = 2


class CarManager:
    def __init__(self):
        self.all_cars = []

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(x=new_x, y=car.ycor())

    def generate(self):
        # Here, we are limiting the chance of car generation in the while loop of main.py by ONLY generating a new_car IF the randomly generated number is ONE
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)
