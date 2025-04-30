from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)

    def move(self):
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10
        self.goto(new_x, new_y)



