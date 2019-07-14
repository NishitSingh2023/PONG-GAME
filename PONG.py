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


