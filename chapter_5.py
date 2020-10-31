# # # age = int(input("Enter your age"))
# # # old_enough_to_get_license = age >= 18
# # # if (old_enough_to_get_license):
# # #     print("Get your DL")
# # # else:
# # #     print("You need to wait until you are 18")
# # # if (age):
# # #     print("hello world")
# # import turtle
# def make_window(col="lightgreen"):
#     wn = turtle.Screen()
#     wn.bgcolor(col)
#     return wn
#
# def make_turtle(col, fill, pen):
#     new_turtle = turtle.Turtle()
#     new_turtle.pensize(pen)
#     new_turtle.color(col, fill)
#     return new_turtle
# #
# # #  Create the screen and a turtle
# # window = make_window()
# # tess = make_turtle("blue", "red", 3)
# # tess.penup()
# # tess.forward(-200)
# # tess.pendown()
# #
# # def draw_bar(t, height):
# #     """Turtle draws the bar graph of given height"""
# #     t.begin_fill()
# #     t.left(90)
# #     t.forward(height)
# #     t.write(" " + str(height))
# #     t.right(90)
# #     t.forward(40)
# #     t.right(90)
# #     t.forward(height)
# #     t.left(90)
# #     t.end_fill()
# #     t.penup()
# #     t.forward(10)
# #     t.pendown()
# #     return t
# #
# # xs = [48,117,200,240,160,260,220]
# #
# # # Draw the bar graph
# #
# # for x in xs:
# #     draw_bar(tess, x)
# #
# # window.mainloop()
#
# # 1
#
# days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# # day_number = int(input("enter the day number"))
# # print("The day is", days[day_number])
#
# # # 2
# # start_day_number = int(input("Enter the starting day of your journey "))
# # slept_count = int(input("Enter the number of nights you slept "))
# # return_day_count = (start_day_number + slept_count % 7) % 7
# # print("You return on: " ,days[return_day_count])
#
# # 3
# # 1 a <= b
# # 2 a < b
# # 3 a < 18 or day != 3
# # 4 a < 18 or day == 3
#
# # 5
# # not p  or not q or r
# #  T T F => False
#
# # 6
# def showGrades(marks):
#     for mark in marks:
#         mark = int(mark)
#         if (mark >= 75):
#             print("First Grade")
#         elif (mark < 75 and mark >= 70):
#             print("Upper Second")
#         elif (mark < 70 and mark >= 60):
#             print("Second")
#         elif (mark < 60 and mark >= 50):
#             print("Third")
#         elif (mark < 50 and mark >= 45):
#             print("F1 Supp")
#         elif (mark < 45 and mark >= 40):
#             print("F2")
#         elif (mark < 40):
#             print("F3")
#
# showGrades([83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
#                      49.9, 45, 44.9, 40, 39.9, 2, 0])
#
# # 8
# import turtle
# def make_window(col="lightgreen"):
#     """Create the window with background color"""
#     wn = turtle.Screen()
#     wn.bgcolor(col)
#     return wn
#
# def make_turtle(col, pen):
#     """Create the turtle with color, width"""
#     new_turtle = turtle.Turtle()
#     new_turtle.pensize(pen)
#     new_turtle.color(col)
#     return new_turtle
#
# #  Create the screen and a turtle
# window = make_window()
# tess = make_turtle("blue", 3)
# tess.speed(10)
# tess.penup()
# tess.forward(-200)
# tess.pendown()
#
# def draw_bar(t, height):
#     """Turtle draws the bar graph of given height"""
#     if height >= 200:
#         t.fillcolor("red")
#     elif height >= 100 and height < 200:
#         t.fillcolor("yellow")
#     elif height >=0 and height < 100:
#         t.fillcolor("green")
#     else:
#         t.fillcolor("white")
#     t.fillcolor()
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     if height < 0:
#         t.penup()
#         t.forward(-20)
#         t.write(" " + str(height))
#         t.forward(20)
#         t.pendown()
#     else:
#         t.write(" " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     return t
#
# xs = [48,117,200,240,160,260,220, -60, -150]
#
# # Draw the bar graph
#
# for x in xs:
#     draw_bar(tess, x)
#
# window.mainloop()
#

# def find_hypot(base, height):
#     x = base ** 2 + height ** 2
#     hyp = x ** 0.5
#     print(hyp)
#
# find_hypot(3, 4)
# find_hypot(8, 4)
# 11
# def check_right_triangle(a, b, c):
#     check = (a ** 2 + b ** 2) ** 0.5
#     if abs(check - c) < 0.000001:
#         return True
#     else:
#         return False
# print(check_right_triangle(3, 4, 5))
# print(check_right_triangle(12, 13, 14))

# 12

def find_max(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

def check_right_triangle(a, b, c):
    max = find_max(a, b, c)
    if c == max:
        check = (a ** 2 + b ** 2) ** 0.5
        if abs(check - c) < 0.000001:
            return True
        else:
            return False
    elif b == max:
        check = (a ** 2 + c ** 2) ** 0.5
        if abs(check - b) < 0.000001:
            return True
        else:
            return False
    else:
        check = (b ** 2 + c ** 2) ** 0.5
        if abs(check - a) < 0.000001:
            return True
        else:
            return False
# print(check_right_triangle(3, 4, 5))
# print(check_right_triangle(3, 5, 4))
# print(check_right_triangle(5, 4, 3))
# print(check_right_triangle(12, 13, 14))
#
# import math
# a = math.sqrt(2.0)
# print(a, a*a)
# print(abs(a ** 2 - 2) < 0.000001)

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx * dx + dy * dy
#     distance = dsquared ** 0.5
#     return distance
# print(distance(0, 4, 0, 0))
# print(distance(7, 8, 2, 900))
# print(distance(1, 1, 33, 0))

def is_divisible(x, y):
    return x % y == 0
# print(is_divisible(3,2))
# print(is_divisible(10,2))
# print(is_divisible(15, 5))
# print(is_divisible(8, 5))
# if is_divisible(18, 4):
#     print("is divisible...")
# else:
#     print("no")

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def absolute_value(x):
    if x >= 0:
        return x
    return  -x
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite()