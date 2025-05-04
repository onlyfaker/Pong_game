# todo/done - 1. create screen
# todo/done - 2. create and move paddle
# todo/done - 3. create another paddle
# todo/done - 4. crete ball and make it move
# todo/done - 5. detect collision with wall and bounce
# todo/done - 6. detect collision with paddle
# todo - 7. detect when paddle misses
# todo - 8. keep score
import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.tracer(0)
screen.listen()
screen.update()

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()

# TODO - at the end FIX the issue where there is a LAG before i can move with onkeypress!!!!
# TODO - not able to move both paddle at the same time
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    screen.update()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    screen.update()

    #detect collision with right paddle and left paddle
    if ball.distance(right_paddle) <50 and ball.xcor()>320 or ball.distance(left_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()
    screen.update()

    if ball.xcor()>380 or ball.xcor()<-380:
        ball.reset_position_ball()
    screen.update()

screen.exitonclick()
