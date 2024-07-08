# Problem 3:
# Write a function that takes a list of words as input and returns the most common word(s) and their frequencies.

# Input:

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Expected Output:

# [('apple', 3), ('banana', 2)]

from collections import Counter


def most_comm(words=None):
    c = Counter(words)
    print(c.most_common())

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
most_comm(words)