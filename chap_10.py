import turtle

# Create Setup
# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Handling keypresses")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()

# Event handlers
# def forward():
#     tess.forward(30)
#
# def right_turn():
#     tess.right(45)
#
# def left_turn():
#     tess.left(45)

def close():
    wn.bye()

# Connect keypress to event handlers
# wn.onkey(forward, "Up")
# wn.onkey(right_turn, "Right")
# wn.onkey(left_turn, "Left")
# wn.onkey(close, "Return")
#
# wn.listen()
# wn.mainloop()

# tess.shape("circle")
# tess.pensize(3)

def move(x, y):
    wn.title("clicked at {0} {1}".format(x, y))
    tess.goto(x, y)

# wn.onclick(move)
# wn.mainloop()

# wn.title("Using a timer")
# tess.shape("turtle")

def timer():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(timer, 60)

# timer()
# wn.mainloop()
# wn.title("Tess becomes traffic light")
def draw_housing(turtle_entity):
    """ Draw a nice housing to hold the traffic lights """
    turtle_entity.pensize(3)
    turtle_entity.color("black", "darkgrey")
    turtle_entity.begin_fill()
    turtle_entity.forward(80)
    turtle_entity.left(90)
    turtle_entity.forward(200)
    turtle_entity.circle(40, 180)
    turtle_entity.forward(200)
    turtle_entity.left(90)
    turtle_entity.end_fill()

#
# draw_housing()
#
# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")
#
# # This variable keeps track of the current state
# state_num = 0
#
# def make_light_blink():
#     global state_num
#     if state_num == 0:
#         tess.penup()
#         tess.forward(70)
#         tess.fillcolor("orange")
#         state_num = 1
#     elif state_num == 1:
#         tess.penup()
#         tess.forward(70)
#         tess.fillcolor("red")
#         state_num = 2
#     else:
#         tess.penup()
#         tess.back(140)
#         tess.fillcolor("green")
#         state_num = 0

# wn.onkey(make_light_blink, "space")
# wn.listen()
# wn.mainloop()

# 1
# pensize = 5
# tess.shape("circle")
# tess.pensize(pensize)
def red():
    tess.color("red")

def green():
    tess.color("green")

def orange():
    tess.color("orange")

def plus():
    global pensize
    pensize += 1
    tess.shapesize(pensize)

# wn.onkey(red, "R")
# wn.onkey(green, "G")
# wn.onkey(orange, "O")
# wn.onkey(plus, "p")
# wn.listen()
# wn.mainloop()

# 2
import turtle
state_num = 0

def make_window(col="lightgreen"):
    wn = turtle.Screen()
    wn.bgcolor(col)
    return wn

def make_turtle(size=1, shape="turtle"):
    new_turtle = turtle.Turtle()
    new_turtle.shape(shape)
    new_turtle.shapesize(size)
    return new_turtle
#
# wn = make_window()
# tess = make_turtle()
# draw_housing()
# tess.right(180)
# tess.forward(100)
# # Bring the turtle in position of green light
# tess.penup()
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")
#


# 3
wn = make_window()      # Make the screen ready
# tess = make_turtle()    # Make a turtle
# draw_housing(tess)      # Make the light hoosing
pess = make_turtle()    # another turtle
# pess.penup()
# pess.left(180)
# pess.forward(100)
# pess.left(90)
draw_housing(pess)      # another housing

# create 3 turtles
t1 = make_turtle(size=3, shape="circle")
t2 = make_turtle(size=3, shape="circle")
t3 = make_turtle(size=3, shape="circle")

# move 4 turtles in position
def get_3_lights_in_position():
    t1.forward(40)
    t1.left(90)
    t1.forward(50)
    t2.forward(40)
    t2.left(90)
    t2.forward(120)
    t3.forward(40)
    t3.left(90)
    t3.forward(190)
    t3.fillcolor("black")
    t2.fillcolor("black")
    t1.fillcolor("black")

get_3_lights_in_position()

# turn the green light on
def initialize():
    t3.fillcolor("green")
    t2.fillcolor("black")
    t1.fillcolor("black")

def timer_street_light():
    global state_num
    if state_num == 0:
        t1.fillcolor("black")
        t3.fillcolor("green")
        t2.fillcolor("black")
        state_num = 1
        wn.ontimer(timer_street_light, 3000)
    elif state_num == 1:
        t1.fillcolor("black")
        t3.fillcolor("black")
        t2.fillcolor("brown")
        state_num = 2
        wn.ontimer(timer_street_light, 1000)
    elif state_num == 2:
        t1.fillcolor("black")
        t3.fillcolor("black")
        t2.fillcolor("orange")
        state_num = 3
        wn.ontimer(timer_street_light, 1000)
    else:
        t1.fillcolor("red")
        t3.fillcolor("black")
        t2.fillcolor("black")
        state_num = 0
        wn.ontimer(timer_street_light, 3100)


wn.ontimer(initialize, 1000)        # Turn green on after 1 sec
timer_street_light()

wn.mainloop()