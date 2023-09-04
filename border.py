from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        
        self.speed(0)
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(300, 0)
        self.pendown()
        self.goto(300, 290)
        self.goto(-300, 290)
        self.goto(-300, -290)
        self.goto(300, -290)
        self.goto(300, 0)