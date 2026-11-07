# PAINT APP STARTER
# Drag with your mouse to draw. Press keys to change colors.
# Keys: r = red, g = green, b = blue, k = black
#       up/down arrows = bigger/smaller brush, c = clear
# Uses turtle, which comes with Python.

import turtle

screen = turtle.Screen()
screen.title("My Paint App")
screen.bgcolor("white")
screen.setup(width=800, height=600)

brush = turtle.Turtle()
brush.shape("circle")
brush.speed(0)       # draw as fast as possible
brush.pensize(5)
brush.color("black")

# --- Drawing with the mouse ---
def draw(x, y):
    brush.ondrag(None)   # pause while we move, so it doesn't lag
    brush.goto(x, y)
    brush.ondrag(draw)

def jump(x, y):
    # Clicking somewhere moves the brush there without drawing a line
    brush.penup()
    brush.goto(x, y)
    brush.pendown()

brush.ondrag(draw)
screen.onclick(jump)

# --- Changing colors ---
def red():
    brush.color("red")

def green():
    brush.color("green")

def blue():
    brush.color("blue")

def black():
    brush.color("black")

# --- Brush size ---
def bigger():
    brush.pensize(brush.pensize() + 2)

def smaller():
    if brush.pensize() > 2:
        brush.pensize(brush.pensize() - 2)

def clear():
    brush.clear()

screen.listen()
screen.onkey(red, "r")
screen.onkey(green, "g")
screen.onkey(blue, "b")
screen.onkey(black, "k")
screen.onkey(bigger, "Up")
screen.onkey(smaller, "Down")
screen.onkey(clear, "c")

turtle.done()

# LEVEL UP IDEAS
# 1. Add more colors (try "purple", "orange", or "pink").
# 2. Add an eraser: a key that sets the color to "white".
# 3. Press s to stamp a shape where the brush is (look up brush.stamp()).
# 4. Change the background color with a key.
