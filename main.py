# todo - 1. create screen
# todo - 2. create and move paddle
# todo - 3. create another paddle
# todo - 4. crete ball and make it move
# todo - 5. detect collision with wall and bounce
# todo - 6. detect collision with paddle
# todo - 7. detect when paddle misses
# todo - 8. keep score
from turtle import Screen, Turtle
# from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.tracer(0)


paddle_left = Turtle()

paddle_left.penup()
paddle_left.goto(350,y=0)
paddle_left.color("white")
paddle_left.shape("square")
paddle_left.shapesize(stretch_len=1,stretch_wid=5)
screen.update()
screen.listen()

def move_up():
    new_y = paddle_left.ycor()+20
    paddle_left.goto(paddle_left.xcor(),new_y)
def move_down():
    new_y = paddle_left.ycor() + -20
    paddle_left.goto(paddle_left.xcor(), new_y)

screen.onkeypress(move_up,"Up")
screen.onkeypress(move_down,"Down")



game_on = True
while game_on:
    screen.update()


screen.exitonclick()
