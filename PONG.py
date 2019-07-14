from turtle import Turtle, Screen, Shape

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