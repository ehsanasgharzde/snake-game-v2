from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('NavajoWhite')
        self.speed(0)

        randx = randint(-280, 240)
        randy = randint(-280, 240)

        self.goto(randx, randy)

    def refresh(self):
        randx = randint(-280, 240)
        randy = randint(-280, 240)

        self.goto(randx, randy)