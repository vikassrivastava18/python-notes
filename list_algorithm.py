# Test driven development
"""
    Key idea is to write automated tests first.
"""

# linear search algorithm: Linear performance, cannot scale well.

"""
Opening a text file:
f = open(filename, "r")
content = f.read()
f.close()
wds = text_to_words(content)
return wds
"""


"""
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    test(search_linear(friends, "Zoe") == 1)
    test(search_linear(friends, "Joe") == 0)
    test(search_linear(friends, "Paris") == 6)
    test(search_linear(friends, "Bill") == -1)

"""

from unit_tester import test

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1


"""
    vocab = ["apple", "boy", "dog", "down",
                              "fell", "girl", "grass", "the", "tree"]
    book_words = "the apple fell from the tree to the grass".split()
    test(find_unknown_words(vocab, book_words) == ["from", "to"])
    test(find_unknown_words([], book_words) == book_words)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
"""


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    return file_content


def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


bigger_vocab = load_words_from_file("vocab.txt").split()
book_words_with_punct = load_words_from_file('alice.txt')
book_words = text_to_words(book_words_with_punct)

# print("Total word count in vocab:", len(bigger_vocab), "Intial 10 are:", bigger_vocab[:10])
# print("Total words in book:", len(book_words), "Initial 10 are:", book_words[:10])
#
# import time
#
# t0 = time.process_time()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.process_time()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

#  Binary Search

# # xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
# # test(search_binary(xs, 20) == -1)
# # test(search_binary(xs, 99) == -1)
# # test(search_binary(xs, 1) == -1)
# for (i, v) in enumerate(xs):
#     test(search_binary(xs, v) == i)


# def search_binary(ls, i):
#     mid_index_now = len(ls) // 2
#     try:
#         probe = ls[mid_index_now]
#     except IndexError:
#         return -1
#     if i == probe:
#         return mid_index_now
#     elif i > probe:
#         return search_binary(ls[mid_index_now+1:],i)
#     else:
#         return search_binary(ls[:mid_index_now],i)

def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
              .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

import time

# xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
# test(search_binary(xs, 20) == -1)
# test(search_binary(xs, 99) == -1)
# test(search_binary(xs, 1) == -1)
# for (i, v) in enumerate(xs):
#     test(search_binary(xs, v) == i)

# t0 = time.process_time()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.process_time()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

# search_binary(bigger_vocab, "magic")
# t0 = time.process_time()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.process_time()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

def remove_adjacent_dups(ls):
    result = []
    new_item = None
    for item in ls:
        if item != new_item:
            result.append(item)
            new_item = item
    return result

# test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
# test(remove_adjacent_dups([]) == [])
# test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
#                                    ["a", "big", "bite", "dog"])


book_words.sort()
book_words = remove_adjacent_dups(book_words)
# print("Only {0} are unique in book".
#                       format(len(book_words)))
# print("The first 100 words are\n{0}".
#            format(book_words[:100]))

# def merge(xs, ys):
#     """ merge sorted lists xs and ys. Return a sorted result """
#     result = []
#     xi = 0
#     yi = 0
#
#     while True:
#         if xi >= len(xs):          # If xs list is finished,
#             result.extend(ys[yi:]) # Add remaining items from ys
#             return result          # And we're done.
#
#         if yi >= len(ys):          # Same again, but swap roles
#             result.extend(xs[xi:])
#             return result
#
#         # Both lists still have items, copy smaller item to result.
#         if xs[xi] <= ys[yi]:
#             result.append(xs[xi])
#             xi += 1
#         else:
#             result.append(ys[yi])
#             yi += 1


def bagcommon(xl, yl):
    """Returns only those items that are present in both lists"""
    result = []
    for i, item in enumerate(xl):
        if item in yl and item not in result:
            result.append(item)
    return result

# print(bagcommon([5,7,11,11,11,12,13], [7,8,11]))


def bagfirst(xl, yl):
    """Return only those items that are present in the first list, but not in the second."""
    result = []
    for i, item in enumerate(xl):
        if item not in yl:
            result.append(item)
    return result
# print(bagfirst([5,7,11,11,11,12,13], [7,8,11]))


def bag_either (xl, yl):
    result = []
    result.extend(xl)
    for item in yl:
        if item not in result:
            result.append(item)
    return result
# print(bag_either([5,7,11,11,11,12,13], [7,8,11]))


"""bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]"""


def bag_diff(xl, yl):
    result = []
    for item in xl:
        if item not in yl:
            result.append(item)
        else:
            yl.remove(item)
    return result
# print(bag_diff([5,7,11,11,11,xl12,13], [7,8,11]))


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy


# test(not share_diagonal(5,2,2,0))
# test(share_diagonal(5,2,3,0))
# test(share_diagonal(5,2,4,3))
# test(share_diagonal(5,2,4,1))

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


# Solutions cases that should not have any clashes
# test(not col_clashes([6,4,2,0,5], 4))
# test(not col_clashes([6,4,2,0,5,7,1,3], 7))

# # More test cases that should mostly clash
# test(col_clashes([0,1], 1))
# test(col_clashes([5,6], 1))
# test(col_clashes([6,5], 1))
# test(col_clashes([0,6,4,3], 3))
# test(col_clashes([5,0,7], 2))
# test(not col_clashes([2,0,1,3], 1))
# test(col_clashes([2,0,1,3], 2))


def has_clashes(board):
    dimension = len(board)
    for i in range(1, dimension):
        if col_clashes(board, i):
            return True
    return False

#
# test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
# test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
# test(has_clashes([0,1,2,3]))             # Try small 4x4 board
# test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case

import random


# Create 100 random boards
def create_boards():
    boards = []
    for i in range(1, 10000):
        board = []
        for j in range(8):
            while True:
                item = random.randrange(0,8)
                if item not in board:
                    board.append(item)
                    break
        boards.append(board)
    return boards


borads = create_boards()

#  Get some solutions
# for board in borads:
#     if not has_clashes(board):
#         print("found a sol:", board)


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def return_common(vocab, book):
    common_words = []
    xi = 0
    yi=0

    while True:
        #  Return the result when probing is impossible in either list
        if xi >= len(vocab) or yi >= len(book):
            return common_words

        # Probe the elements
        if vocab[xi] == book[yi]:
            common_words.append(vocab[xi])
            xi += 1
            yi += 1
        elif vocab[xi] < book[yi]:
            xi +=1
        else:
            yi +=1


# common_words = return_common(bigger_vocab, book_words)

# Return only those items that are present in the first list, but not in the second.

def first_only(vocab, book):
    first_only_words = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            return first_only_words

        if vocab[xi] < book[yi]:
            first_only_words.append(vocab[xi])
            xi += 1
        elif vocab[xi] > book[yi]:
            yi += 1
        else:
            xi +=1; yi +=1


def present_in_either(vocab, book):
    present_in_either_words = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):          # If xs list is finished,
            present_in_either_words.extend(book[yi:]) # Add remaining items from book
            return present_in_either_words          # And we're done.

        if yi >= len(book):          # Same again, but swap roles
            present_in_either_words.extend(vocab[xi:])
            return present_in_either_words

        # Both lists still have items, copy smaller item to result.
        item = None
        if vocab[xi] < book[yi]:
            present_in_either_words.append(vocab[xi])
            xi += 1
        elif vocab[xi] > book[yi]:
            present_in_either_words.append(book[yi])
            yi += 1
        else:
            if vocab[xi] !=item:
                present_in_either_words.append(vocab[xi])
            xi +=1; yi +=1


def bag_diff2(vocab, book):
    bag_diff_list = []
    xi = 0
    yi = 0
    counter = 0
    while True:
        if xi >= len(vocab):
            return bag_diff_list
        if yi >= len(book):
            bag_diff_list.extend(vocab[xi:])
            return bag_diff_list

        if vocab[xi] < book[yi]:
            bag_diff_list.append(vocab[xi])
            xi += 1
        elif vocab[xi] > book[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1

# print(bag_diff2([5,7,11,11,11,12,13], [7,8,11]))


def queen(board):
    """Find 10 solutions for the given board"""
    t0 = time.process_time()
    size = board
    solutions = []
    for i in range(3000000):
        start_list = list(range(board))
        random.shuffle(start_list)
        # Write the diagonal test here
        if not has_clashes(start_list) and start_list not in solutions:
            solutions.append(start_list)
    t1 = time.process_time()
    return {"length": len(solutions), "time": t1-t0}

# print(queen(16))


""""Queen board
    [[0, 0, 0, 0, 0, q, 0, 0],   [1, 3, 4, 5, 2, 0, 7, 6] -> [2, 7, 3, 6, 5, 4, 0, 1]
     [q, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, q, 0, 0, 0],
     [0, q, 0, 0, 0, 0, 0, 0],
     [0, 0, q, 0, 0, 0, 0, 0],
     [0, 0, 0, q, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, q],
     [0, 0, 0, 0, 0, 0, q, 0],
    ]
    board = [1, 0, 3, 5, 4, 7, 6, 2]
    mirror_y = [2, 6, 7, 4, 5, 3, 0, 1] -> solution[0] = board[-1], solution[1] = board[-2]
    mirror_x = [2, 6, 7, 4, 5, 3, 0, 1] -> solution[0] = 7 - board[0]
"""


def mirror_y(board):
    solution = []

    for i, item in enumerate(board):
        index = -(i+1)
        solution.append(board[index])
    return solution


# print(mirror_y([2, 6, 7, 4, 5, 3, 0, 1]))

def mirror_x(board):
    solution = []
    for item in board:
        print(item)
        solution.append(7-item)
    return solution

# print(mirror_x([2, 6, 7, 4, 5, 3, 0, 1]))


def transform_90(board):
    solution = []
    counter = 0
    while len(solution) < 8:
        for i, item in enumerate(board):
            if item == counter:
                solution.append(7-i)
                counter += 1

    return solution


print(transform_90([1, 3, 4, 5, 2, 0, 7, 6]))

