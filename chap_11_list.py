students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

counter = 0

import turtle

a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a[0])
# for (name, subjects) in students:
#     if "CompSci" in subjects:
#         counter += 1
# print("number of students taking computer science is:", counter)

# 1
# If start is greater than end step < 0 # If start is greater than end step > 0
import turtle

# tess = turtle.Turtle()
# alex = tess
# alex.color("hotpink")
# print(alex is tess)
# print(tess.color())
# Only one instance is created, both bind to the same value. Changing color of tess changes color of alex also

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def add_vectors(u, v):
    result = []
    for (i, val) in enumerate(v):
        result.append(v[i] + u[i])
    return result
# test(add_vectors([1, 1], [1, 1]) == [2, 2])
# test(add_vectors([1, 2], [1, 4]) == [2, 6])
# test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

def scalar_mult(s, v):
    result = []
    for (i, val) in enumerate(v):
        result.append(val*s)
    return result
# test(scalar_mult(5, [1, 2]) == [5, 10])
# test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
# test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

def dot_product(u, v):
    result = 0
    for (i, val) in enumerate(v):
        result += v[i] * u[i]
    return result
test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

# The vectors are in X, Y plane
def cross_product(u, v):
    return  [u[0]*v[1] - u[1]*v[0]] + "-k"

#9
song = 'rain in Spain...'
song_mod = " ".join(song.split())

#10
def replace(word, f, w):
    split = word.split(f)
    join = w.join(split)
    return join

# test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
# test(replace(s, "om", "am") ==
#     "I love spam! Spam is my favorite food. Spam, spam, yum!")
#
# test(replace(s, "o", "a") ==
#     "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
a = ["This", "is", "fun"]
b = [2, 3, 4]

# def swap(x, y):  # Incorrect version
#     global a, b
#     (a, b) = (y, x)

# def swap(x, y):  # Incorrect version
#     return (y, x)


# print("before swap function call: a:", a, "b:", b)
# swap(a, b)
# print("after swap function call: a:", a, "b:", b)



