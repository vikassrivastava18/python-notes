import random
import unit_tester
rng = random.Random()
cards = list(range(52))
rng.shuffle(cards)

def make_random_ints(num, lower, upper):
    """Make random list allowing repetition"""
    random_list = []
    for i in range(num):
        random_list.append(rng.randrange(lower, upper))
    return random_list

def make_random_ints_without_dup(num, lower, upper):
    """Make random list without repetiton"""
    list_init = list(range(lower, upper))
    rng.shuffle(list_init)
    return list_init[:num]

def make_rangdm_list_from_large_range(num, lower, upper):
    result = []
    for i in range(num):
        while True:
            item = rng.randrange(lower, upper)
            if item not in result:
                result.append(item)
                break
    return result

def make_random_list_from_large2(num, lower, upper):
    ls = list(range(1, 1000000))
    rng.shuffle(ls)
    return ls[:5]

# for i in range(5):
#     print(make_random_ints(5, 1, 10))
#
# for i in range(5):
#     print(make_random_ints_without_dup(5, 1, 10))
#
# for i in range(5):
#     print(make_rangdm_list_from_large_range(5, 1, 1000000))

# import time
#
# t0 = time.perf_counter()
# print(make_rangdm_list_from_large_range(5, 1, 1000000))
# t1 = time.perf_counter()
# print(t1-t0)
#
# t2 = time.perf_counter()
# print(make_random_list_from_large2(5, 1, 1000000))
# t3 = time.perf_counter()
# print(t3-t2)

# import ex_module
# string = "hello world"
# print(ex_module.remove_at(6, string))
from unit_tester import test

import calendar

# cal = calendar.TextCalendar()
# cal.pryear(2012)

#2
# 44 functions

#7
def myreplace(old, new, s):
    split_it = s.split(" ")
    list = []
    for ls in split_it:
        if not ls == "":
            list.append(ls)
    join = " ".join(list)
    split_again = join.split(old)
    return new.join(split_again)
# print(myreplace(" ", "**", "Words will now      be  separated by stars."))


# test(myreplace(",", ";", "this, that, and some other thing") ==
#                          "this; that; and some other thing")
# test(myreplace(" ", "**",
#                  "Words will now      be  separated by stars.") ==
#                  "Words**will**now**be**separated**by**stars.")

#8
from  string import punctuation

punc_list = list(punctuation)

def cleanword(word):
    out_string = ''
    for char in word:
        if char not in punc_list:
          out_string += char
    return out_string

# print(cleanword("what?"))
# test(cleanword("what?") == "what")
# test(cleanword("'now!'") == "now")
# test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")


def has_dashdash(word):
    return word.find("--") != -1
#
# test(has_dashdash("distance--but"))
# test(not has_dashdash("several"))
# test(has_dashdash("spoke--"))
# test(has_dashdash("distance--but"))
# test(not has_dashdash("-yo-yo-"))

def extract_words(word):
    clean_word = cleanword(word)
    word_lower = clean_word.lower()
    return word_lower.split()

print(extract_words("she tried to curtsey as she spoke--fancy"))
# test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
#       ['now','is','the','time','now','is','the','time','yes','now'])
# test(extract_words("she tried to curtsey as she spoke--fancy") ==
#       ['she','tried','to','curtsey','as','she','spoke','fancy'])

def wordcount(word, word_list):
    count = 0
    for w in word_list:
        if w == word:
            count += 1
    return count

# test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
# test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
# test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
# test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

def wordset(word_list):
    out_list = []
    for word in word_list:
        if not word in out_list:
            out_list.append(word)
    out_list.sort()
    return out_list

# print(wordset(["now", "is", "time", "is", "now", "is", "is"]))
#
# test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
#       ["is", "now", "time"])
# test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
#       ["I", "a", "am", "is"])
# test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
#       ["a", "am", "are", "be", "but", "is", "or"])

def longestword(word_list):
    import math
    smallest = 0
    if not len(word_list):
        return 0
    for word in word_list:
        longest = max(smallest, len(word))
    return longest

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)