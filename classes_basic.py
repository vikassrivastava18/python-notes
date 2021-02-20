
# Procedural programming:
# Write procedures which operate on data

# OOP:
# Create objects whech contains both data and procedures(functionality)


class Point:
    """Point class represents and manipulates x, y cordinates"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y **2) ** 0.5

    def halfway(self, target):
        mid_x = (self.x + target.x) /2
        mid_y = (self.y + target.y) /2
        return Point(mid_y, mid_y)

    def distance(self, target):
        return ((self.x-target.x)**2 + (self.y-target.y)**2) ** 0.5

    def get_line_to(self, target):
        try:
            slope = (target.y - self.y) / (target.x - self.x)
            c = self.y - slope * self.x
        except ZeroDivisionError:
            return "Equation of line: x = {0}".format(self.x)
        return (slope, c)

    def reflect_x(self):
        return Point(self.x, -self.y)

    def slope_from_origin(self):
        try:
            slope = self.y/self.x
        except ZeroDivisionError:
            return "Infinity"
        return slope

    # def center_of_circle(self, p1, p2, p3):
    #     side1 = self.get_line_to(self, p1)
    #     side1 =

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(3, 4)
p2 = Point(0, 6)

half_w = p1.halfway(p2)

print(Point(6, 11).get_line_to(Point(6, 15)))


class SMS_store:
    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        unread_messages = 0
        for item in self.messages:
            if not item[0]:
                unread_messages += 1
        return unread_messages

    def get_message(self, i):
        item_count = int(i)
        try:
            message = self.messages[i]
        except:
            return None
        return message

    def delete(self, i):
        item_count = int(i)
        del self.messages[item_count]
        return None

    def clear(self):
        self.messages.clear()
        return None


my_inbox = SMS_store()
my_inbox.add_new_arrival("9205731743", "12:30", "Hello World")

print(my_inbox.get_message(0))










