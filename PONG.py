from turtle import Turtle, Screen, Shape
from random import randint

# Making Screen
screen = Screen()
screen.setup(600, 400)

# Playing Field Boundaries
play_top = screen.window_height() / 2 - 100
play_bottom = -screen.window_height() / 2 + 100
play_left = -screen.window_height() / 2 + 50
play_right = screen.window_height() / 2 - 50

# Draw PlayGround
area = Turtle()
area.hideturtle()

area.pensize(10)
area.penup()
area.goto(play_left, play_top)
area.pendown()
area.goto(play_right, play_top)
area.goto(play_right, play_bottom)
area.goto(play_left, play_bottom)
area.goto(play_left, play_top)

# BALL
ball = Turtle()

ball.penup()
ball.shape("circle")
ball.shapesize(0.5, 0.5)

ball_radius = 10 * 0.5

# Paddles
L = Turtle()
R = Turtle()
L.penup()
R.penup()

# Paddle shape
paddle_w_half = 10 / 2      # 10 units wide
paddle_h_half = 40 / 2      # 40 units high
paddle_shape = Shape("compound")
paddle_points = ((-paddle_h_half, -paddle_w_half),
                 (-paddle_h_half, paddle_w_half),
                 (paddle_h_half, paddle_w_half),
                 (paddle_h_half, -paddle_w_half))
paddle_shape.addcomponent(paddle_points, "black")
screen.register_shape("paddle", paddle_shape)
L.shape("paddle")
R.shape("paddle")

L.setx(play_left + 10)
R.setx(play_right - 10)

# Score
score = Turtle()
score.hideturtle()
score.penup()

score_L = 0
score_R = 0

def write_score():
    score.clear()
    score.goto(-screen.window_width() / 4, screen.window_height() / 2 - 80)
    score.write(score_L, align="center", font=("Arial", 32, "bold"))
    score.goto(screen.window_width() / 4, screen.window_height() / 2 - 80)
    score.write(score_R, align="center", font=("Arial", 32, "bold"))

write_score()

screen.tracer()

def frame():
    check_if_someone_scores()
    update_paddle_positions()
    update_ball_position()
    screen.update()
    screen.ontimer(frame, framerate_ms)

# Start the game
framerate_ms = 40
frame()

# ball_movement speed
ball_move_xaxis = 3     #speed of ball in horizontally
ball_move_yaxis = 2     #speed of ball in vertically

def update_ball_position():
    global ball_move_xaxis, ball_move_yaxis

    if ball.ycor()+ball_radius >= play_top:
        ball_move_yaxis *= -1
    if ball.ycor()-ball_radius <= play_bottom:
        ball_move_yaxis *= -1

    ball.setx(ball.xcor() + ball_move_xaxis)
    ball.sety(ball.ycor() + ball_move_xaxis)

def reset_ball():
    global ball_move_xaxis, ball_move_yaxis

    ball.setpos(0, 0)

    speed_horiz = randint(2, 4)
    speed_vert = randint(2, 4)

    direction_horiz = 1
    direction_vert = 1

    if randint(0, 100) > 50:  # 50% chance of going left instead of right
        direction_horiz = -1
    if randint(0, 100) > 50:  # 50% chance of going down instead of up
        direction_vert = -1

    ball_move_xaxis = direction_horiz * speed_horiz
    ball_move_yaxis = direction_vert * speed_vert

def check_if_someone_scores():
    global score_L, score_R
    if ball.xcor()+ball_radius > play_right:
        score_L += 1
        write_score()
        reset_ball()
    if ball.xcor()+ball_radius > play_left:
        score_R += 1
        write_score()
        reset_ball()

def update_paddle_positions():
    pass