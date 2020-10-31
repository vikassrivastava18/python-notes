
# tess.shape("turtle")
# tess.color("blue")
#
# tess.penup()                # This is new
# size = 20
# for i in range(30):
#    # tess.color("pink")
#    tess.stamp()             # Leave an impression on the canvas
#    size = size + 3          # Increase the size on every iteration
#    tess.forward(size)       # Move tess along
#    tess.right(24)           #  ...  and turn her
#    tess.color("pink")


# Draw multicolored square
import turtle
__import__("turtle").__traceable__ = False
import random
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.right(0)
colors = ["red", "blue", "green", "yellow", "purple", "pink", "black"]
start = 0
size = 10
angle = 0
print(colors[2])
def draw_square(size, start, color_index, angle):
    tess.forward(start)
    tess.right(angle)
    for i in range(4):
       tess.color(colors[color_index])
       tess.forward(size)
       tess.left(90)
for j in range(4):
   for i in range(7):
       draw_square(size, start, i, angle)
       size += 5
       start =size / 5
       angle = 18

wn.mainloop()


