# todo/done - 1. create screen
# todo/done - 2. create and move paddle
# todo/done - 3. create another paddle
# todo - 4. crete ball and make it move
# todo - 5. detect collision with wall and bounce
# todo - 6. detect collision with paddle
# todo - 7. detect when paddle misses
# todo - 8. keep score
from turtle import Screen, Turtle

from paddle import Paddle


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.tracer(0)
screen.update()
screen.listen()

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

# TODO - at the end FIX the issue where there is a LAG before i can move with onkeypress!!!!
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_on = True
while game_on:

    screen.update()


screen.exitonclick()
