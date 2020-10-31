import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def absolute_value(n):
    if n > 0:
        return n
    else:
        return -n

# def test_suite():
#     """ Run the suite of tests for code in this module (this file).
#     """
#     test(absolute_value(17) == 17)
#     test(absolute_value(-17) == 17)
#     test(absolute_value(0) == 0)
#     test(absolute_value(3.14) == 3.14)
#     test(absolute_value(-3.14) == 3.14)
#
# test_suite()

# 1
def turn_clockwise(c):
    directions = ["N", "E", "S", "W"]
    for d in range(4):
        if c == "W":
            return "N"
        elif c == directions[d]:
            return  directions[d + 1]
    return None

# def test_suite():
#     """ Run the suite of tests for code in this module (this file).
#     """
#     test(turn_clockwise("N") == "E")
#     test(turn_clockwise("E") == "S")
#     test(turn_clockwise("S") == "W")
#     test(turn_clockwise("W") == "N")
#     test(turn_clockwise("Wild") == None)
#
# test_suite()

# 2
def day_name(n):
    if type(n) != int or n > 6 or n < 0:
        return None
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(7):
        return days[n]

# def test_suite():
#     """ Run the suite of tests for code in this module (this file).
#     """
#     test(day_name(0) == "Sunday")
#     test(day_name(1) == "Monday")
#     test(day_name(6) == "Saturday")
#     test(day_name("W") == None)
#     test(day_name(-12) == None)
#
# test_suite()

# 3
def day_num(day_input):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    count = 0
    for day in days:
        if day_input == day:
            return count
        count += 1
    return None
# def test_suite():
#     test(day_num("Friday") == 5)
#     test(day_num("Sunday") == 0)
#     test(day_num(day_name(3)) == 3)
#     test(day_name(day_num("Thursday")) == "Thursday")
#     test(day_num("Halloween") == None)
#
# test_suite()

def day_add(day, add):
    remaining = add % 7
    day_count = day_num(day)
    final_count = (day_count + remaining) % 7
    return day_name(final_count)

# def test_suite():
#     test(day_add("Monday", -7) == "Monday")
#     test(day_add("Tuesday", -10) == "Saturday")
#     test(day_add("Saturday", -9) == "Thursday")
#     test(day_add("Sunday", -100) == "Friday")
# test_suite()

# 6
days_table = [
        {"month": "January", "days": 31},
        {"month": "February", "days": 28},
        {"month": "March", "days": 31},
        {"month": "April", "days": 30},
        {"month": "May", "days": 31},
        {"month": "June", "days": 30},
        {"month": "July", "days": 31},
        {"month": "August", "days": 31},
        {"month": "September", "days": 30},
        {"month": "October", "days": 31},
        {"month": "November", "days": 30},
        {"month": "December", "days": 31}
]

def days_in_month(month_in):
    for month in days_table:
        if month["month"] == month_in:
            return month["days"]
    return None
# def test_suite():
#     test(days_in_month("February") == 28)
#     test(days_in_month("December") == 31)
#     test(days_in_month("hello") == None)
#
# test_suite()


# 7, 8, 9
def to_secs(h, m , s):
    return int(h * 3600 + m * 60 + s)

def hours_in(sec):
    return sec // 3600

def minutes_in(sec):
    return (sec % 3600) // 60

def seconds_in(sec):
    return ((sec % 3600) % 60)

# def test_suite():
#     test(to_secs(2, 30, 10) == 9010)
#     test(to_secs(2, 0, 0) == 7200)
#     test(to_secs(0, 2, 0) == 120)
#     test(to_secs(0, 0, 42) == 42)
#     test(to_secs(0, -10, 10) == -590)
#     test(to_secs(2.5, 0, 10.71) == 9010)
#     test(to_secs(2.433, 0, 0) == 8758)
#     test(hours_in(9010) == 2)
#     test(minutes_in(9010) == 30)
#     test(seconds_in(9010) == 10)
# test_suite()

# 12
def hypotenuse(b, h):
    hyp_square = b ** 2 + h ** 2
    return round(hyp_square ** 0.5)
#
# def test_suite():
#     test(hypotenuse(3, 4) == 5.0)
#     test(hypotenuse(12, 5) == 13.0)
#     test(hypotenuse(24, 7) == 25.0)
#     test(hypotenuse(9, 12) == 15.0)
# test_suite()

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def is_odd(c):
    return is_even(c + 1)

# def test_suite():
#     test(is_even(11) == False)
#     test(is_even(12) == True)
#     test(is_odd(11) == True)
#     test(is_odd(12) == False)
# test_suite()

def is_factor(a, b):
    if b % a == 0:
        return True
    return False

# def test_suite():
#     test(is_factor(3, 12))
#     test(not is_factor(5, 12))
#     test(is_factor(7, 14))
#     test(not is_factor(7, 15))
#     test(is_factor(1, 15))
#     test(is_factor(15, 15))
#     test(not is_factor(25, 15))
# test_suite()

def is_multiple(a,b):
    return is_factor(b, a)

def test_suite():
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
test_suite()