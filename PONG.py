from turtle import Turtle, Screen, Shape
from random import randint

# Making Screen
screen = Screen()
screen.setup(600, 400)
screen.tracer(0)

# Playing Field Boundaries
play_top = screen.window_height() / 2 - 100
play_bottom = -screen.window_height() / 2 + 100
play_left = -screen.window_height() / 2 + 50
play_right = screen.window_height() / 2 - 50

# Draw PlayGround
area = Turtle()
area.hideturtle()

area.penup()
area.goto(play_left, play_top)
area.pensize(5)
area.pendown()
area.goto(play_right, play_top)
area.pensize(5)
area.pencolor('red')
area.goto(play_right, play_bottom)
area.pensize(5)
area.pencolor('black')
area.goto(play_left, play_bottom)
area.pensize(5)
area.pencolor('red')
area.goto(play_left, play_top)

'''area.pensize(5)
area.pencolor('black')
area.
'''

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

# move them into postion
L.setx(play_left + 10)
R.setx(play_right - 10)

# Paddle movement
paddle_L_move_direction = 0
paddle_R_move_direction = 0

paddle_move_vert = 6


def paddle_is_allowed_to_move_here(new_pos):
    if play_bottom > new_pos - paddle_h_half:
        return False
    if play_top < new_pos + paddle_h_half:
        return False
    return True

def update_paddle_positions():
    L_new_y_pos = L.ycor() + (paddle_L_move_direction * paddle_move_vert)
    R_new_y_pos = R.ycor() + (paddle_R_move_direction * paddle_move_vert)
    if paddle_is_allowed_to_move_here(L_new_y_pos):
        L.sety(L_new_y_pos)
    if paddle_is_allowed_to_move_here(R_new_y_pos):
        R.sety(R_new_y_pos)


def L_up():
    global paddle_L_move_direction
    paddle_L_move_direction = 1


def L_down():
    global paddle_L_move_direction
    paddle_L_move_direction = -1


def R_up():
    global paddle_R_move_direction
    paddle_R_move_direction = 1


def R_down():
    global paddle_R_move_direction
    paddle_R_move_direction = -1


def L_off():
    global paddle_L_move_direction
    paddle_L_move_direction = 0


def R_off():
    global paddle_R_move_direction
    paddle_R_move_direction = 0


screen.onkeypress(L_up, "w")
screen.onkeypress(L_down, "s")
screen.onkeypress(R_up, "Up")
screen.onkeypress(R_down, "Down")
screen.onkeyrelease(L_off, "w")
screen.onkeyrelease(L_off, "s")
screen.onkeyrelease(R_off, "Up")
screen.onkeyrelease(R_off, "Down")
screen.listen()


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


def check_if_someone_scores():
    global score_L, score_R
    if (ball.xcor() + ball_radius) >= play_right:  # right of ball at right of field
        score_L += 1
        write_score()
        reset_ball()
    elif play_left >= (ball.xcor() - ball_radius):  # left of ball at left of field
        score_R += 1
        write_score()
        reset_ball()

# BALL
ball = Turtle()

ball.penup()
ball.shape("circle")
ball.shapesize(0.5, 0.5)

ball_radius = 10 * 0.5

# ball_movement speed
ball_move_xaxis = 9     #speed of ball in horizontally
ball_move_yaxis = 6     #speed of ball in vertically

def ball_collides_with_paddle(paddle):
    x_distance = abs(paddle.xcor() - ball.xcor())
    y_distance = abs(paddle.ycor() - ball.ycor())
    overlap_horizontally = (ball_radius + paddle_w_half >= x_distance)
    overlap_vertically = (ball_radius + paddle_h_half >= y_distance)
    return overlap_horizontally and overlap_vertically   # returns either true or false


def update_ball_position():
    global ball_move_xaxis, ball_move_yaxis
    if ball.ycor() + ball_radius >= play_top:  # top of ball at or above top of field
        ball_move_yaxis *= -1
    elif play_bottom >= ball.ycor() - ball_radius:  # bottom of ball at or below bottom of field
        ball_move_yaxis *= -1
    if ball_collides_with_paddle(R) or ball_collides_with_paddle(L):
        ball_move_xaxis *= -1
    ball.setx(ball.xcor() + ball_move_xaxis)
    ball.sety(ball.ycor() + ball_move_yaxis)

def reset_ball():
    global ball_move_xaxis, ball_move_yaxis

    ball.setpos(0, 0)

    speed_horiz = randint(5, 8)
    speed_vert = randint(5, 8)

    direction_horiz = 1
    direction_vert = 1

    if randint(0, 100) > 50:  # 50% chance of going left instead of right
        direction_horiz = -1
    if randint(0, 100) > 50:  # 50% chance of going down instead of up
        direction_vert = -1

    ball_move_xaxis = direction_horiz * speed_horiz
    ball_move_yaxis = direction_vert * speed_vert


# Frames
def frame():
    check_if_someone_scores()
    update_paddle_positions()
    update_ball_position()
    screen.update()
    screen.ontimer(frame, framerate_ms)


# Start the game
write_score()
framerate_ms = 40
frame()
