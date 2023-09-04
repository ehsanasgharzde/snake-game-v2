from turtle import Turtle
 

STARTPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in STARTPOSITIONS:
            self.addsegment(position)

    def addsegment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)

        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(2000, 2000)

        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[segnum - 1].xcor()
            ycor = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(xcor, ycor)

        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)