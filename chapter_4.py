# # # def NAME( PARAMETERS ):
# # #     STATEMENTS
# # import turtle
# # def draw_square(t, sz):
# #     for i in range(4):
# #         t.forward(sz)
# #         t.left(90)
# #     return t
# # def make_setup():
# #     wn = turtle.Screen()
# #     wn.bgcolor("lightgreen")
# #     return wn
# # w = make_setup()
# # tess = turtle.Turtle()
# # draw_square(tess, 100)
# # w.mainloop()
# # import random
# # import turtle
# # def make_window(colr, tit):
# #     wn = turtle.Screen()
# #     wn.bgcolor(colr)
# #     wn.title(tit)
# #     return wn
# #
# # def make_turtle(col, sz):
# #     t = turtle.Turtle()
# #     t.color(col)
# #     rand_angle = random.randrange(0,90)
# #     t.left(rand_angle)
# #     t.forward(100)
# #     return t
# #
# # wn = make_window("pink", "hello world")
# # t1 = make_turtle("yellow", 10)
# # t2 = make_turtle("red", 15)
# # t3 = make_turtle("green", 20)
# # wn.mainloop()
#
# # def get_final_amount(amt, rate, comp, year):
# #     final_amt = amt * (1 + rate / comp) ** (comp * year)
# #     return final_amt
# # print(get_final_amount(100, 0.1, 1, 3))
# # import turtle
# # def make_window(colr, ttle):
# #     """
# #       Set up the window with the given background color and title.
# #       Returns the new window.
# #     """
# #     w = turtle.Screen()
# #     w.bgcolor(colr)
# #     w.title(ttle)
# #     return w
# #
# #
# # def make_turtle(colr, sz):
# #     """
# #       Set up a turtle with the given color and pensize.
# #       Returns the new turtle.
# #     """
# #     t = turtle.Turtle()
# #     t.color(colr)
# #     t.pensize(sz)
# #     return t
# #
# #
# # wn = make_window("lightgreen", "Tess and Alex dancing")
# # tess = make_turtle("hotpink", 5)
# # alex = make_turtle("black", 1)
# # dave = make_turtle("yellow", 2)
# # wn.mainloop()
# # 4.9
import turtle
#
# # 1
# def make_window():
#     """Create a screen for turtle"""
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     return wn
# #
def make_square(t, sz):
    """Create a turtle of required size"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
# #
# # def pen_up(t, x):
# #     t.penup()
# #     t.forward(x)
# #     t.pendown()
# #
# # #  Create screen and turtle
# # window = make_window()
# # tess = turtle.Turtle()
# # tess.color("purple")
# # pen_up(tess, -100)    # Move tess to the left
# #
# # for i in range(5):
# #     make_square(tess, 40)
# #     pen_up(tess, 70)
# # window.mainloop()
#
# # 2
def make_window(col):
    """Create a screen for turtle"""
    wn = turtle.Screen()
    wn.bgcolor(col)
    return wn
#
def make_turtle(col):
    t = turtle.Turtle()
    t.color(col)
    return t
#
# def make_square(t, sz):
#     """Make square with the turtle"""
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
#     return t
#
# def move_turtle(t, x, y):
#     t.penup()
#     t.forward(-x)
#     t.right(90)
#     t.forward(y)
#     t.left(90)
#     t.pendown()
#     return t
# window = make_window("green")
# tess = make_turtle("purple")
# size = 20
# # Make 5 squares
# for i in range(5):
#     make_square(tess, size)
#     size += 20
#     move_turtle(tess, 10, 10)
# window.mainloop()

# 3
# window = make_window("lightgreen")
# tess = make_turtle("red")
# tess.pensize(10)
# def draw_poly(t, n, sz):
#     sides = int(n)
#     angle = 360 / sides
#     for side in range(sides):
#         t.forward(sz)
#         t.left(angle)
# draw_poly(tess, 8, 50)
# window.mainloop()

# 4
# window = make_window("lightgreen")
# tess = make_turtle("red")
# tess.pensize(2)
# for i in range(20):
#     make_square(tess,80)
#     tess.right(18)
# window.mainloop()

# 5
# window = make_window("lightgreen")
# tess = make_turtle("blue")
# tess.forward(-100)
# tess.speed(15)
# side = 5
#
# for i in range(100):
#     tess.forward(side)
#     side += 2
#     tess.right(90)
# side = 5
# pess = make_turtle("blue")
# pess.speed(15)
# pess.penup()
# pess.forward(150)
# pess.pendown()
# for i in range(100):
#     pess.forward(side)
#     pess.right(92)
#     side +=2
#
#
# # 6
# def draw_polynomial(t, sides, length):
#     sides = int(sides)
#     angle = 360 / sides
#     for side in range(sides):
#         t.forward(length)
#         t.left(angle)
#
# def draw_equilateral(t, sz):
#     draw_polynomial(t, 3, sz)
# tess = make_turtle("yellow")
# draw_equilateral(tess, 100)

# 9
window = make_window("lightgreen")
tess = make_turtle("blue")
def draw_star(t, side):
    for i in range(5):
       t.forward(side)
       t.right(144)

# draw_star(tess, 100)

# 10
for i in range(5):
    draw_star(tess, 80)
    tess.penup()
    tess.forward(300)
    tess.right(144)
    tess.pendown()

window.mainloop()
