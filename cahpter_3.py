# 3.1
# for i in range(1000):
#     print("We like Python's turtles")
#
# # 3.2
# # Attributes
# # RAM, CPU, Camera Quality,
# # Methods
# # Make a call, Start the wifi, browse the internet
#
# # 3.3
#
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", \
#           "October", "Novenber", "December"]
# for month in months:
#     print("One of the months of the year is", month)

# 3.4
# Tess completes 10 circles and is 45 Deg NE

# 3.5
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# # a
# for x in xs:
#     print(x)
# # b
# for x in xs:
#     print(x * x)
# # c
# total = 0
# for x in xs:
#     total += x
# print("Sum of the numbers is", total)
# # d
# total = 1
# for x in xs:
#     total *= x
# print("Multiplications of the numbers equals", total)

# 6
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()

# def draw_regular_polygon(sides, sidelength):
#     # Setup
#     sides = int(sides)
#     angle = 360 / sides
#     for side in range(sides):
#         alex.forward(sidelength)
#         alex.left(angle)
# draw_regular_polygon(3,  40)
# draw_regular_polygon(4, 45)
# draw_regular_polygon(5, 50)
# draw_regular_polygon(6,60)
# draw_regular_polygon(8,80)


# #7
# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# total = 0
# drunk_alex = turtle.Turtle()
# drunk_alex.shape("turtle")
# for angle in angles:
#     drunk_alex.left(angle)
#     drunk_alex.forward(100)
#     total +=angle
# print("heading of alex is", total)     # answer for 8

#9
# 360 / 18 = 20

# 10
# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.right(90)
# tess.left(3600)
# tess.right(-90)
# tess.speed(10)
# tess.left(3600)
# tess.speed(0)
# tess.left(3645)
# tess.forward(-100)
# wn.mainloop()

# 11
import random
# wn = turtle.Screen()
# tess = turtle.Turtle()
# print(type(tess))
# angle = 50
# tess.left(angle)
# tess.forward(100)
# for i in range(4):
#     tess.right(144)
#     tess.forward(100)
# wn.mainloop()

# 12
wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(1)
tess.shape("turtle")
tess.penup()
angle = 0
dash = turtle.Turtle()
dash.speed(1)
dash.shape("arrow")
dash.penup()

def common_steps(t, d):
    # void fuction
    t.forward(d)
    t.stamp()
    t.forward(-d)
    t.right(30)

def make_clock():
    for i in range(12):
        common_steps(tess, 100)
        common_steps(dash, 80)
make_clock()

wn.mainloop()











