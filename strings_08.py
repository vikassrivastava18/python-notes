import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
# # word = 'hello world'
# # print(word.upper())
# # print(list(word))
# # print(list(enumerate(word))
# # )
# count = 0
# # while count < len(word):
# #     letter = word[count]
# #     print(letter)
# #     count += 1
# #
# # for letter in word:
# #     print(letter)
#
# def remove_vowels(word):
#     vowels = 'aeiou'
#     out = ''
#     for letter in word:
#         if letter.lower() not in vowels:
#             out += letter
#     return out
#
# # test(remove_vowels("compsci") == "cmpsc")
# # test(remove_vowels("aAbEefIijOopUus") == "bfjps")
#
# def find(strng, ch, start=0, end=None):
#     """
#       Find and return the index of ch in strng.
#       Return -1 if ch does not occur in strng.
#     """
#     ix = start
#     if end is None:
#         end = len(strng)
#     while ix < end:
#         if strng[ix] == ch:
#             return ix
#         ix += 1
#     return -1
#
# test(find("Compsci", "p") == 3)
# test(find("Compsci", "p", 3) == 3)
# test(find("Compsci", "p", 4) == -1)
# test(find("Compsci", "C") == 0)
# test(find("Compsci", "c", 2) == 5)
# test(find("Compsci", "i") == 6)
# test(find("Compsci", "x") == -1)
#
# ss = "Python strings have some interesting methods."
# test(find(ss, "s") == 7)
# test(find(ss, "s", 7) == 7)
# test(find(ss, "s", 8) == 13)
# test(find(ss, "s", 8, 13) == -1)
# test(find(ss, ".") == len(ss)-1)
#
# ss = "Well I never did said Alice"
# print(ss.split())
#
# import string
# punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
# def remove_punctuation(para):
#     out = ""
#     for letter in para:
#         if letter not in string.punctuation:
#             out += letter
#     return out
#
# test(remove_punctuation('"Well, I never did!", said Alice.') ==
#                             "Well I never did said Alice")
# test(remove_punctuation("Are you very, very, sure?") ==
#                              "Are you very very sure")
#
# my_story = """
# Pythons are constrictors, which means that they will 'squeeze' the life
# out of their prey. They coil themselves around their prey and with
# each breath the creature takes the snake will squeeze a little tighter
# until they stop breathing completely. Once the heart stops the prey
# is swallowed whole. The entire animal is digested in the snake's
# stomach except for fur or feathers. What do you think happens to the fur,
# feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
# you guessed it --- snake POOP! """
#
# # wds = remove_punctuation(my_story).split()
# # print(wds)
#
# s1 = "My name is {0}".format("Vikas")
# print(s1)
#
# name = "Alice"
# age = 10
# s2 = "She is {0}, and she is {1} years old".format("Alice", 10)
# print(s2)
#
# n1 = 4
# n2 = 5
# s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
# print(s3)

# print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
# for i in range(1, 11):
#     print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",
#                                             i**10, "\t", i**20)

layout = "{0:>4}{1:>4}{2:>6}{3:>8}{4:>13}{5:>24}"
# print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
# for i in range(11):
#     print(layout.format(i, i**2, i**3, i**5, i**10, i**20))

prefixes = "JKLMNOPQM"
suffix = "ack"

# for letter in prefixes:
#     if letter == "Q" or letter == "O":
#         letter += "u"
#     print(letter + suffix)
# 3
def count_letters(fruit, letter):
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    return(count)
# print(count_letters("banana", "n"))


def find_pos(word, letter, start):
    letter_pos = word.find(letter, start)
    return letter_pos

def count_letters(fruit, letter):
    count = 0
    start = 0
    while True:
        letter_pos = fruit.find(letter, start)
        if letter_pos != -1:
            count += 1
            start = letter_pos + 1
            # print(start)
        else:
            break
    return(count)
# print(find_pos("banana", "n", 0))
# print(find_pos("banana", "n", 2))
# print(find_pos("banana", "n", 4))
# print(count_letters('ananaanananananana', 'a'))
# print(count_letters('banana', 'a'))
# print(count_letters('banana', 'n'))
# print(count_letters('banana', 'b'))
# print(count_letters('ananaanananananana', 'n'))

# 5

para = """
So far we have seen built-in types like int
, float, bool, str and we’ve seen lists and pairs. Strings, 
lists, and pairs are qualitatively different from the others 
because they are made up of smaller pieces. In the case of strings, 
they’re made up of smaller strings each containing one character.
"""

# word_list = para.split(" ")
# print(word_list)

# 6
def draw_table():
    # first line header
    print("{0:<4}{1:<4}{2:<4}{3:<4}{4:<4}{5:<4}{6:<4}{7:<4}{8:<4}{9:<4}{10:<6}{11:<6}{12:<8}".format
    ("\t    ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    dash = ""
    for i in range(55):
        dash += "-"
    print("    :", dash)
    for i in range(1,13):
        print(" {0:<2}".format(i), ":  ", "{0:<4}{1:<4}{2:<4}{3:<4}{4:<4}{5:<4}{6:<4}{7:<4}{8:<4}{9:<6}{10:<6}{11:<8}".format
              (i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9,  i*10,  i*11,  i*12))
# draw_table()

# word = "hello"
# reverse = ""
# for i in range(len(word)):
#     reverse += word[len(word)-i-1]
# print(reverse)
def reverse(word):
    reverse = ""
    for i in range(len(word)):
        reverse += word[len(word)-i-1]
    return reverse
# test(reverse("happy") == "yppah")
# test(reverse("Python") == "nohtyP")
# test(reverse("") == "")
# test(reverse("a") == "a")

# 8
def mirror(word):
    word_reverse = reverse(word)
    word += word_reverse
    return word
# test(mirror("good") == "gooddoog")
# test(mirror("Python") == "PythonnohtyP")
# test(mirror("") == "")
# test(mirror("a") == "aa")

# 9
def remove_letter(letter, word):
    result = ''
    for w in word:
        if w == letter:
            continue
        result += w
    return result
#
# test(remove_letter("a", "apple") == "pple")
# test(remove_letter("a", "banana") == "bnn")
# test(remove_letter("z", "banana") == "banana")
# test(remove_letter("i", "Mississippi") == "Msssspp")

def is_palindrome(word):
    reverse_word = reverse(word)
    if word == reverse_word:
        return True
    return False

# test(is_palindrome("abba"))
# test(not is_palindrome("abab"))
# test(is_palindrome("tenet"))
# test(not is_palindrome("banana"))
# test(is_palindrome("straw warts"))
# test(is_palindrome("a"))
# test(is_palindrome(""))

def remove(extract, word, start=1, end=None):
    pos = word.find(extract,start)
    if pos != -1:
        # result = word[start:pos] + word[pos+len(extract):end]
        # Mississippi
        # result = word[0:1] + word[4:]
        result = word[0:pos] + word[pos+len(extract):]

    else:
        result = word
    return result
# test(remove("an", "banana") == "bana")
# test(remove("cyc", "bicycle") == "bile")
# test(remove("iss", "Mississippi") == "Missippi")
# test(remove("eggs", "bicycle") == "bicycle")
# print(remove("an", "banana"))

def get_position(ext, word, start=0):
    return word.find(ext, start)

def index_all(ext, word):
    index = 0
    index_list = []
    while True:
        get_pos = get_position(ext, word, index)
        if get_pos != -1:
            index_list.append(get_pos)
            index = get_pos + 1
        else:
            break
    return index_list

def remove_all(ext, word):
    index_list = index_all(ext, word)
    print(index_list)
    result = word
    for item in index_list:
        result = remove(ext, result, 0)
        print(result)
    # print(result)

remove_all("iss", "Mississipiabcisshellomiss")