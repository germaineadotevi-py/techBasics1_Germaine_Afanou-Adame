# Generative Art - Refactored Version
# Put comments here about what your program does and how to use it

# Import libraries
from turtle import *

# Some examples of potential constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
BACKGROUND_COLOR = 'white'


def setup_canvas():
    setup(CANVAS_WIDTH, CANVAS_HEIGHT)
    tracer(0, 0)  # Turn off animation
    bgcolor(BACKGROUND_COLOR)
    # ... and more setup as you need

# wrap complicated shapes into functions
def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)

def draw_star():
    pass

def move_to():
    pass

def main_design():
    # your for looks and drawing code here
    pass

def main():
    # focus on giving an overview of the general structure of your game here
    setup_canvas()
    main_design()
    update() # update canvas, important to keep right before done
    done() # important to keep at the end!

if __name__ == "__main__":
    main()
