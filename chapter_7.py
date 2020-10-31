# def sum_to(n):
#     sum = 0
#     for count in range(n + 1):  # range(n + 1) --> [0, 1, 2, ...., n]
#         sum += count
#     return sum
# print(sum_to(10))
# print(sum_to(1000))
#
# def seq3np1(n):
#     """Reach 1 either by halving or (3 * n) + 1"""
#     while n != 1:
#         print(n, end=" ,")
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#     print(n, end=".\n")
#
# def check_collatz():
#     for i in range(2,10000):
#         j = i
#         steps = 0
#         while i != 1:
#             steps += 1
#             if i % 2 == 0:
#                 i = i // 2
#             else:
#                 i = 3 * i + 1
#         print(j, "follows collatz conjencture", "required steps: ", steps)
#
# # check_collatz()
#
# # seq3np1(9896)
#
# def num_digits(n):
#     count = 0
#     if n == 0:
#         count = 1
#     while n != 0:
#         n = n // 10
#         count += 1
#     return count
#
# print(num_digits(12))
# print(num_digits(120))
# print(num_digits(1))
# print(num_digits(0))
# # print(num_digits(-100))   Infinite loop
#
# def num_zero_or_five(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         if digit == 0 or digit == 5:
#             count += 1
#         n = n // 10
#     return count
#
# # print(num_zero_or_five(100300550))
# # print(num_zero_or_five(1055030250))
#
# # for x in range(11):
# #     print(x, "\t", 2**x)
# def multiplication_table(n):
#     for i in range(1, 11):
#         print(n * i, end='  ')
#     print()
#
# def table_upto_ten():
#     for i in range(2, 11):
#         multiplication_table(i)

# table_upto_ten()
# total = 0
# while True:
#     response = input("Enter a number or blank to exit")
#     if response == "":
#         break
#     total += int(response)
# print("totla of your numbers is: ", total)


import random  # We cover random numbers in the

rng = random.Random()  # modules chapter, so peek ahead.
number = rng.randrange(1, 10)  # Get random number between [1 and 1000).

guesses = 0
msg = ""

# while True:
#     guess = int(input(msg + "\nGuess my number between 1 and 10: "))
#     guesses += 1
#     if guess > number:
#         msg += str(guess) + " is too high.\n"
#     elif guess < number:
#         msg += str(guess) + " is too low.\n"
#     else:
#         break
#
# input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))

# def multiplication_table(n):
#     for i in range(1, n+1):
#         print(n * i, end='\t')
#     print('\n')
#
# def table_upto_ten():
#     for i in range(1, 11):
#         multiplication_table(i)
#
# table_upto_ten()

def sqrt(n):
    guess = n/2.0
    steps = 0
    while True:
        steps += 1
        better = (guess + n/guess)/2
        if abs(guess - better) < 0.001:
            return better, steps
        guess = better
# Test cases
# print(sqrt(25.0))
# print(sqrt(49.0))
# print(sqrt(81.0))
# print(sqrt(5))
# print(sqrt(70))

# for i in range(1, 1000):
#     print(sqrt(i))

# EXERCISE

# 1
ls = [2, 4, 5, 7, 1, 11, 34, 111, 58]

def count_odd(ls):
    count = 0
    for item in ls:
        if item % 2 == 1:   # Condition for odd
            count += 1
    return count
# print(count_odd(ls))

# 5
def skip_first_even(ls):
    total = 0
    count = 0
    for item in ls:
        if item % 2 == 0:
            count += 1
            if count == 1:
                continue
        total += item
    return total
# print(skip_first_even(ls))
# print(skip_first_even([1, 2, 3, 6]))
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(skip_first_even([1, 2, 3, 6]) == 10)
    test(skip_first_even([1, 7, 3, 5]) == 16)
    test(skip_first_even([1, 7, 3, 5, 10]) == 16)
    test(skip_first_even([10, 7, 3, 5]) == 15)

# test_suite()
# print(skip_first_even([1, 2, 3, 7, 2]))

# 7
def sqrt(n):
    guess = n/2.0
    steps = 0
    while True:
        steps += 1
        better = (guess + n/guess)/2
        print(better)
        if abs(guess - better) < 0.001:
            return better, steps
        guess = better

# sqrt(25)

# 9
def print_triangular_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
        print(i, '\t', total)

# print_triangular_numbers(5)

# 10
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def test_prime():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(49))
    test(is_prime(51))
    test(not is_prime(495))
    test(not is_prime(99))
    test(is_prime(97))


# test_prime()
# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

# 11
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# alex_motion = [(160, 20), (-43, 10), (270, 8), (-43, 12), (100, 23), (-23, 24),
#                (160, 20), (-43, 10), (270, 8), (-43, 12), (100, 23), (-23, 24),
#                (160, 20), (-43, 10), (270, 8), (-43, 12), (100, 23), (-23, 24)]
# total = 0
# drunk_alex = turtle.Turtle()
# drunk_alex.shape("turtle")

# for (angle, steps) in alex_motion:
#     drunk_alex.left(angle)
#     drunk_alex.forward(steps)

# 12
# sqrt_2  = sqrt(2)
# house_points =[(0, 50), (135, 70.5), (-75, 50), (-60, 50), (-120, 50)]
# for (angle, steps) in house_points:
#     drunk_alex.left(angle)
#     drunk_alex.forward(steps)

#14
def num_digits(n):
    count = 0
    n = abs(n)
    if n == 0:
        count = 1
    while n != 0:
        n = n // 10
        count += 1
    return count
test(num_digits(0) == 1)
test(num_digits(-12345) == 5)

# 15
def num_even_digits(n):
    count = 0
    if n == 0:
        count = 1
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n = n // 10
    return count
# test(num_even_digits(123456) == 3)
# test(num_even_digits(2468) == 4)
# test(num_even_digits(1357) == 0)
# test(num_even_digits(0) == 1)

# 16
def sum_of_squares(xs):
    total = 0
    for x in xs:
        total += x ** 2
    return total
# test(sum_of_squares([2, 3, 4]) == 29)
# test(sum_of_squares([ ]) == 0)
# test(sum_of_squares([2, -3, 4]) == 29)

# 17
def play_with_comp(human):
    import random
    rng = random.Random()
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} ".format(human, result))
    return result


def the_luck_game():
    player_score = 0
    computer_score = 0
    drawn = 0
    while True:
        choice = str(input("Hit i to play or leave blank, press quit to quit the gane - "))
        if choice == "quit":
            print("Goodbye!, final score-- You won {0}, Comp Won {1}, draw {2}".format(player_score, computer_score, drawn))
            break
        elif choice == '':
            result = play_with_comp(False)
        else:
            result = play_with_comp(True)
        if result == 0:
            drawn += 1
        elif result == 1:
            player_score += 1
        else:
            computer_score += 1
        print("score-- You won {0}, Comp Won {1}, draw {2}".format(player_score, computer_score, drawn))

# the_luck_game()

