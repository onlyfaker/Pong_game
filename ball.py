from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.y_move = 10
        self.x_move = 10


    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move*=-1

    def reset_position_ball(self):
        self.goto(0,0)
        self.bounce_x()

