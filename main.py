# todo/done - 1. create screen
# todo/done - 2. create and move paddle
# todo/done - 3. create another paddle
# todo/done - 4. crete ball and make it move
# todo/done - 5. detect collision with wall and bounce
# todo - 6. detect collision with paddle
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

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    screen.update()



screen.exitonclick()
