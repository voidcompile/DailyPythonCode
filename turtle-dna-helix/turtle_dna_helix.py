import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("DNA Double Helix")

helix = turtle.Turtle()
helix.speed(0)
helix.pensize(2)
helix.hideturtle()

base_pair = turtle.Turtle()
base_pair.speed(0)
base_pair.pensize(1)
base_pair.hideturtle()

# Colors for DNA ladder
colors = ["cyan", "magenta", "yellow", "lime"]

# Drawing parameters
amplitude = 100  # Height of sine wave
wavelength = 10  # Number of base pairs between connections
step = 5         # Distance between each step (not used explicitly here)
length = 360     # Number of steps (longer = longer helix)

# Draw two sinusoidal DNA strands
for i in range(length):
    angle = math.radians(i * 4)
    x = i - length / 2
    y1 = amplitude * math.sin(angle)
    y2 = -amplitude * math.sin(angle)

    color = colors[i % len(colors)]
    
    # First strand nucleotide
    helix.penup()
    helix.goto(x, y1)
    helix.pendown()
    helix.pencolor(color)
    helix.dot(6)

    # Second strand nucleotide
    helix.penup()
    helix.goto(x, y2)
    helix.pendown()
    helix.pencolor(color)
    helix.dot(6)

    # Base pair connecting the two strands
    if i % wavelength == 0:
        base_pair.penup()
        base_pair.goto(x, y1)
        base_pair.pendown()
        base_pair.pencolor("white")
        base_pair.goto(x, y2)

# Exit on click
screen.exitonclick()
