# SNAKE STARTER
# Eat the food to grow longer. Don't hit the walls or yourself!
# Controls: arrow keys.
# Uses turtle, which comes with Python.

import turtle
import random

STEP = 20  # size of one square

# --- Set up the screen ---
screen = turtle.Screen()
screen.title("My Snake")
screen.bgcolor("darkgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- The snake's head ---
head = turtle.Turtle()
head.shape("square")
head.color("lightgreen")
head.penup()
head.direction = "stop"

body = []  # the rest of the snake goes in this list

# --- The food ---
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()

def move_food():
    food.goto(random.randint(-14, 14) * STEP, random.randint(-14, 14) * STEP)

move_food()

# --- The score ---
score = 0
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def show_score():
    pen.clear()
    pen.write("Score: " + str(score), align="center", font=("Courier", 20, "bold"))

show_score()

# --- Steering (no turning straight back into yourself) ---
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

def move_head():
    if head.direction == "up":
        head.sety(head.ycor() + STEP)
    if head.direction == "down":
        head.sety(head.ycor() - STEP)
    if head.direction == "left":
        head.setx(head.xcor() - STEP)
    if head.direction == "right":
        head.setx(head.xcor() + STEP)

def reset_game():
    global score
    head.goto(0, 0)
    head.direction = "stop"
    for part in body:
        part.hideturtle()
    body.clear()
    score = 0
    show_score()

# --- The game loop ---
def game_loop():
    global score

    # Eat the food: grow one square longer
    if head.distance(food) < STEP:
        move_food()
        part = turtle.Turtle()
        part.shape("square")
        part.color("green")
        part.penup()
        body.append(part)
        score = score + 1
        show_score()

    # Each body part moves to where the part in front of it was
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())
    if body:
        body[0].goto(head.xcor(), head.ycor())

    move_head()

    # Hit a wall?
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        reset_game()

    # Hit yourself?
    for part in body:
        if part.distance(head) < STEP / 2:
            reset_game()
            break

    screen.update()
    screen.ontimer(game_loop, 120)  # smaller number = faster snake

game_loop()
turtle.done()

# LEVEL UP IDEAS
# 1. Make the snake speed up as it gets longer.
# 2. Keep a high score that stays when you restart.
# 3. Add golden food worth 3 points.
# 4. Let the snake wrap around to the other side instead of hitting walls.
