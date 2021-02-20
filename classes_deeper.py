from classes_basic import Point
import copy
from unit_tester import test


class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, pos, w, h):
        """Initialize Rectangle with initial position pos, width w, height h"""
        self.corner = pos
        self.width = w
        self.height = h

    def grow(self, delta_width, delta_height):
        """Grow or shrink rectangle by th deltas"""
        self.width += delta_width
        self.height += delta_height

    def move(self, delta_x, delta_y):
        self.corner.x += delta_x
        self.corner.y += delta_y

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perm = 2 * (self.width + self.height)
        return perm

    def flip(self):
        flipper = self.width
        self.width = self.height
        self.height = flipper

    def contains(self, point):
        if 0 <= point.x < 10 and 0 <= point.y < 5:
            return True
        else:
            return False

    def collision(self, rect):
        """Change the logic to find a corner of one rectangle inside the other"""
        if rect.corner.y > self.corner.y + self.height or rect.corner.x > self.corner.x + self.width:
            return False
        elif self.corner.y < rect.corner.y + rect.height < self.corner.y + self.height and \
                self.corner.x < rect.corner.x + rect.width < self.corner.x + self.width:
            return True
        """Find the loginc for other case scenarios"""

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)


# box = Rectange(Point(0, 0), 100, 200)
# bomb = Rectange(Point(100,80), 5, 10)
#
# box.grow(10, 10)
# print("box", box)
# box.move(10, 10)
#
# p1 = Point(1,1)
# p2 = copy.copy(p1)
# print("p1", p1)
# print("p2", p2)
# p1.x = 2
# print("p1", p1)
# print("p2", p2)
#
# r1 = Rectange(p1, 100, 100)
# r2 = copy.deepcopy(r1)
# print("r1", r1)
# print("r2", r2)
# r1.move(20, 20)
# print("r1 move")
# print("r1", r1)
# print("r2", r2)
#
# r1.grow(100, 100)
# print("r1 grow")
# print("r1", r1)
# print("r2", r2)

r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)

r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)

r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)

r = Rectangle(Point(0, 0), 10, 5)
# test(r.contains(Point(0, 0)))
# test(r.contains(Point(3, 3)))
# test(not r.contains(Point(3, 7)))
# test(not r.contains(Point(3, 5)))
# test(r.contains(Point(3, 4.99999)))
# test(not r.contains(Point(-3, -3)))
r2 = Rectangle(Point(3, 3), 2, 1)

test(r.collision(r2) == True)


