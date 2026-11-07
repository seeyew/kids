# PONG STARTER
# Keep the ball from getting past your paddle.
# Controls: Up and Down arrow keys.
# Uses turtle, which comes with Python.

import turtle

# --- Set up the screen ---
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # we redraw the screen ourselves, so it runs smoothly

# --- The paddle ---
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)  # tall and thin
paddle.penup()
paddle.goto(-350, 0)

# --- The ball ---
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.dx = 3   # how far the ball moves sideways each step
ball.dy = 3   # how far the ball moves up/down each step

# --- The score ---
score = 0
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def show_score():
    pen.clear()
    pen.write("Score: " + str(score), align="center", font=("Courier", 24, "bold"))

show_score()

# --- Moving the paddle ---
def paddle_up():
    if paddle.ycor() < 250:
        paddle.sety(paddle.ycor() + 30)

def paddle_down():
    if paddle.ycor() > -250:
        paddle.sety(paddle.ycor() - 30)

screen.listen()
screen.onkeypress(paddle_up, "Up")
screen.onkeypress(paddle_down, "Down")

# --- The game loop: runs over and over ---
def game_loop():
    global score
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off the top and bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = -ball.dy

    # Bounce off the right wall
    if ball.xcor() > 390:
        ball.dx = -ball.dx

    # Hit the paddle!
    if -350 < ball.xcor() < -330 and abs(ball.ycor() - paddle.ycor()) < 55:
        ball.dx = -ball.dx
        score = score + 1
        show_score()

    # Missed! Start the ball again from the middle
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 3
        score = 0
        show_score()

    screen.update()
    screen.ontimer(game_loop, 16)  # about 60 times a second

game_loop()
turtle.done()

# LEVEL UP IDEAS
# 1. Make the ball faster each time you hit it (try ball.dx = ball.dx * 1.1).
# 2. Change the colors or make the paddle smaller for a harder game.
# 3. Add a second paddle on the right for a friend (use the W and S keys).
# 4. Show "Game Over" after 3 misses.
