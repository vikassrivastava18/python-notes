import unit_tester
# Dictionary methods
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears":100}

# for k in inventory:   # inventory.keys()
#     print(k, inventory[k])
#
# print(inventory.values())

# for (k, v) in inventory.items():
#     print(k, v)

# print("apples" in inventory)
# print("bananas" in inventory)
# print("peaches" in inventory)

copy_inventory = inventory.copy()
copy_inventory["bananas"] = 0
# print("copy_inventory", copy_inventory, "inventory", inventory)
copy2_inventory = inventory
copy2_inventory["bananas"] = 0
# print("copy2_inventory", copy_inventory, "inventory", inventory)

matrix = {(0, 0): 9, (1, 4): 5}
# print(matrix.get((1, 1), 0))


"""Memoization - A previously computed value that is stored for later use is called a memo."""
alreadyknown = {0: 0, 1: 1}
def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


import time
t1 = time.process_time()
print(fib(999))
t2 = time.process_time()
print(t2-t1)
print(alreadyknown)
letters_count = {}
word = "Mississippi"

for char in word:
    letters_count[char] = letters_count.get(char, 0) + 1
# print(letters_count)


"""
Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order 
which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample
 output of the program when the user enters the data “ThiS is String with Upper and lower case Letters”, would look this this:
 """
def char_count_print():
    import re
    out_dict = {}
    inp_str = input("Enter a string")
    inp_str = re.sub(" ", "", inp_str)
    for char in inp_str.lower():
        out_dict[char] = out_dict.get(char, 0) + 1
    out_list = list(out_dict.items())
    out_list.sort()
    for (k, v) in out_list:
        print(k, v)


def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return


from unit_tester import test
# new_inventory = {}
# add_fruit(new_inventory, "strawberries", 10)
# test("strawberries" in new_inventory)
# test(new_inventory["strawberries"] == 10)
# add_fruit(new_inventory, "strawberries", 25)
# test(new_inventory["strawberries"] == 35)

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
      "abcdefghijklmnopqrstuvwxyz"
      )

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds_list = cleaned_text.split()
    return wds_list

"""
Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical listing
of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. (You
can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.) The first 10
lines of your output file should look something like this:
"""

alice_text = load_words_from_file('alice.txt')
alice_text_list = text_to_words(alice_text)
alice_text_list.sort()
word_dict = {}

for word in alice_text_list:
    word_dict[word] = word_dict.get(word, 0) + 1

# print("Word", '\t\t', "Count")
# for (key, val) in word_dict.items():
#     print(key, "\t\t", val)
#
# print(word_dict['alice'])
#
# # Longest word in the book
# longest_word = ''
# for key in word_dict.keys():
#     if len(key) > len(longest_word):
#         longest_word = key
# print("longest_word", longest_word)

