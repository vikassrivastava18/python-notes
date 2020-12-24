# import turtle
#
# import random
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.forward(-200)
# turtle.speed(10)
#
#
# def koch(t, order, size):
#     """
#        Make turtle t draw a Koch fractal of 'order' and 'size'.
#        Leave the turtle facing the same direction.
#     """
#
#     if order == 0:          # The base case is just a straight line
#         t.forward(size)
#     else:
#         koch(t, order-1, size/3)   # Go 1/3 of the way
#         t.left(60)
#         koch(t, order-1, size/3)
#         t.right(120)
#         koch(t, order-1, size/3)
#         t.left(60)
#         koch(t, order-1, size/3)
#
#
# koch(tess, 6, 1000)
#
# wn.mainloop()


def r_num(nested_element_list):
    total = 0
    for item in nested_element_list:
        if type(item) == list:
            total += r_num(item)
        else:
            total += item

    return total


print("sum of nested list", r_num([1, 2, [11, 13, 1, 2, 3], 8]))

import math


def r_max(num_list):
    largest = -math.inf
    for item in num_list:
        if type(item) == list:
            largest = max(largest, r_max(item))
        else:
            largest = max(item, largest)
    return largest


from unit_tester import test

test(r_max([2, 9, [1, 13], 8, 6]) == 13)
test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
# test(r_max(["joe", ["sam", "ben"]]) == "sam")


def fib(num):
    if num <= 1:
        return num
    else:
        result = fib(num - 1) + fib(num - 2)
    return result


# import time
# t0 = time.clock()
# n = 35
# result = fib(n)
# t1 = time.clock()
#
# print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

# import pygame, math
#
# pygame.init()  # prepare the pygame module for use
#
# # Create a new surface and window.
# surface_size = 1024
# main_surface = pygame.display.set_mode((surface_size, surface_size))
# my_clock = pygame.time.Clock()


# def draw_tree(order, theta, sz, posn, heading, color=(0, 0, 0), depth=0):
#     trunk_ratio = 0.29  # How big is the trunk relative to whole tree?
#     trunk = sz * trunk_ratio  # length of trunk
#     delta_x = trunk * math.cos(heading)
#     delta_y = trunk * math.sin(heading)
#     (u, v) = posn
#     newpos = (u + delta_x, v + delta_y)
#     pygame.draw.line(main_surface, color, posn, newpos)

    # if order > 0:  # Draw another layer of subtrees
    #
    #     # These next six lines are a simple hack to make the two major halves
    #     # of the recursion different colors. Fiddle here to change colors
    #     # at other depths, or when depth is even, or odd, etc.
    #     if depth == 0:
    #         color1 = (255, 0, 0)
    #         color2 = (0, 0, 255)
    #     else:
    #         color1 = color
    #         color2 = color
    #
    #     # make the recursive calls to draw the two subtrees
    #     newsz = sz * (1 - trunk_ratio)
    #     draw_tree(order - 1, theta, newsz, newpos, heading - theta, color1, depth + 1)
    #     draw_tree(order - 1, theta, newsz, newpos, heading + theta, color2, depth + 1)


# def gameloop():
#     theta = 0
#     while True:
#
#         # Handle evente from keyboard, mouse, etc.
#         ev = pygame.event.poll()
#         if ev.type == pygame.QUIT:
#             break;
#
#         # Updates - change the angle
#         theta += 0.01
#
#         # Draw everything
#         main_surface.fill((255, 255, 0))
#         draw_tree(9, theta, surface_size * 0.9, (surface_size // 2, surface_size - 50), -math.pi / 2)
#
#         pygame.display.flip()
#         my_clock.tick(120)


# gameloop()
# pygame.quit()
#
#
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.speed(10)


def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def snow_flake(t, n, size):
    for i in range(3):
        koch(t, n-1, size)
        t.right(120)

# snow_flake(tess, 4, 300)
#
# wn.mainloop()

# def ctl_fractal(n):
#     if n== 0:
#         tess.forward(10)
#     else:
#         for i in [85, 190, 85, 0]:
#             ctl_fractal(n-1)
#             tess.right(i)
#
#
# def ctl_2_fractal(t):
#     for i in [85, 190, 85, 0]:
#         tess.forward(20)
#         tess.right(i)
#
#
# def ctl_3_fractal(t):
#     for i in [85, 190, 85, 0]:
#         ctl_2_fractal(t)
#         tess.right(i)
#
#
# def ctl_4_fractal(t):
#     for i in [85, 190, 85, 0]:
#         ctl_3_fractal(t)
#         tess.right(i)

#
# tess.forward(-100)
# ctl_fractal(6)


# def cesaro_square(n, size):
#     for i in range(4):
#         ctl_fractal(n-1)
#         tess.right(90)


# cesaro_square(4, 100)


def sierpinski_tri_0(t, size):
    for i in [120, 120, 120]:
        t.left(i)
        t.forward(size)



def sierpinski_tri_1(t, size):
    for i in [0, 60, 0]:
        sierpinski_tri_0(t, size/3)
        t.left(i)
        t.forward(size/3)

#
# sierpinski_tri_1(tess, 100)
# wn.mainloop()


def recursive_min(ls):
    minimum = math.inf
    for item in ls:
        if not type(item) == list:
            minimum = min(minimum, item)
        else:
            minimum = min(minimum, recursive_min(item))
    return minimum

# test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
# test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
# test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
# test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)


def count(num, ls):
    c = 0
    for item in ls:
        if type(item) == list:
            c += count(num, item)
        else:
            if item == num:
                c +=1
    return c

# test(count(2, []) == 0)
# test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
# test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
# test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
# test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
# test(count("a",
#      [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)



def flatten(ls):
    final = []

    """Add all the elements recursively"""
    if not type(ls) == list:
        return ls
    for item in ls:
        if type(item) == list:
            for i in item:
                final.append(flatten(i))
        else:
            final.append(item)
    print("final", final)
    return final


test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])

# print(flatten([2,9,[2,1,13,2],8,[2,6]]))