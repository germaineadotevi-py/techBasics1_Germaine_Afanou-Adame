### Basic Turtle cheatsheet

# import libraries
from turtle import *
import random

# initial setup: canvas size
width = 400
height = 400


setup(width, height)
# turn off animation, comment it out to see the drawing process
tracer(0, 0)
# hide turtle cursor
hideturtle()
# set background color
bgcolor('white') # You can either use color names
# change the color of the lines
color('#000') # Or Hex Code

# draw rotating lines
for i in range(4):
    # always move to the same point
    penup()
    goto(100, -100) # lower right corner
    pendown()
    right(20)
    forward(50)
    backward(100) # add this to make the lines cross in center

# after rotation, remember to rotate back
# to the default direction: East (to the right)
left(80)

# move to lower left corner
penup()
goto(-150,-150)
pendown()

# draw triangle
for i in range(3):
    forward(100) # draw from starting point, go forward
    left(120) # turn right 90 degree

# move to upper left corner
penup()
goto(-180,180)
pendown()

# draw square
for i in range(4):
    forward(100) # draw from starting point, go forward
    right(90) # turn right 90 degree

# move to the center
penup()
goto(0,0)
pendown()

# draw circle
fillcolor("blue")
begin_fill()
circle(50, 360) # radius & angle
end_fill()

update() # update canvas, important to keep right before done
done() # important to keep at the end!