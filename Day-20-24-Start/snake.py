from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.segments_num = 0
        self.init_snake()
        self.head = self.segments[0]
        self.head.color("green")

    def init_snake(self):
        for position in STARTING_POSITIONS:
            if self.segments_num % 2 == 0:
                self.add_segment(position, "chartreuse")
            else:
                self.add_segment(position, "spring green")

    def add_segment(self, position, color):
        new_segment = Turtle("square")
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.segments_num += 1

    def extend(self):
        if self.segments_num % 2 == 0:
            self.add_segment(self.segments[-1].position(), "chartreuse")
        else:
            self.add_segment(self.segments[-1].position(), "spring green")

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)

        self.head.forward(MOVE_DISTANCE)

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

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.init_snake()
        self.head = self.segments[0]
