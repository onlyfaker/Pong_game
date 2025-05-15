# todo/done - 1. create screen
# todo/done - 2. create and move paddle
# todo/done - 3. create another paddle
# todo/done - 4. crete ball and make it move
# todo/done - 5. detect collision with wall and bounce
# todo/done - 6. detect collision with paddle
# todo/done - 7. detect when paddle misses
# todo/done - 8. keep score
import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

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
scoreboard= Scoreboard()

# TODO - at the end FIX the issue where there is a LAG before i can move with onkeypress!!!!
# TODO - not able to move both paddle at the same time
# TODO - make the ball start moving when space is press

screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

ball_speed = 0.1
game_on = True
while game_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    screen.update()

# detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    screen.update()

# detect collision with right paddle and left paddle
    if ball.distance(right_paddle) <50 and ball.xcor()>320 or ball.distance(left_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()
        if ball_speed>0.005:
            ball_speed -=0.005
    screen.update()

# detect R paddle miss
    if ball.xcor()>380:
        scoreboard.score_count_player1+=1
        ball_speed=0.1
        time.sleep(1)
        scoreboard.increase_score()
        ball.reset_position_ball()

# detect L paddle miss
    if ball.xcor()<-380:
        scoreboard.score_count_player2+=1
        ball_speed=0.1
        time.sleep(1)
        scoreboard.increase_score()
        ball.reset_position_ball()
    screen.update()

screen.exitonclick()
