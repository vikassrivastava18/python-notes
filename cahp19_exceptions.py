import turtle
import time

def show_poly():
    sides = input("How many sides do you want in your polygon?")
    try:
        # This dialog could be cancelled,
        #   or the conversion to int might fail, or n might be zero.
        win = turtle.Screen()  # Grab/create a resource, e.g. a window
        tess = turtle.Turtle()
        n = int(sides)
        angle = 360 / n
        for i in range(n):      # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)           # Make program wait a few seconds
    finally:
        win.bye()               # Close the turtle's window


def readposint2():
    inp = input("Enter a positive integer")
    try:
        pos_int = int(inp)
        if pos_int < 0:
             my_error = ValueError("You entered a negative number&quot")
             raise my_error
        print(pos_int)
    except Exception as e:
        print(e)
    finally:
        print("Program ends execution")

show_poly()
readposint2()

