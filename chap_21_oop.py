""" Even more OOP """


class MyTime:

    def __init__(self, hrs=0, mns=0, secs=0):
        self.hours = hrs
        self.minutes = mns
        self.seconds = secs

    def __str__(self):
        return "Time - {0} hours : {1} minutes : {2} seconds".format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        self.hours += seconds // 3600
        left_over = seconds % 3600
        self.minutes += left_over // 60
        self.seconds += left_over % 60


#
# tim1 = MyTime(19, 53, 0)
# print(tim1)


# Pure function, does not modify the objects passed, has no side effects
def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
    sum_t = MyTime(h, m, s)
    return sum_t


def add_time(t1, t2):

    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds

    if s >= 60:
        s -= 60
        m += 1

    if m >= 60:
        m -= 60
        h += 1

    sum_t = MyTime(h, m, s)
    return sum_t


class Point:
    # Previously defined methods here...

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(3, 4)
p2 = Point(5, 7)
print(p1+p2)
