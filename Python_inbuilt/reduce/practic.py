# Problem 1: Multiply All Elements
# Multiply all elements in a list of numbers.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
abc = reduce(lambda x, y: x * y, numbers)
print(abc)
aaa = map()


# Problem 2: Find the Longest String
# Given a list of strings, find the longest string.
words = ["apple", "banana", "cherry", "date"]
result = reduce(lambda x, y : x if len(x) > len(y) else y, words)
print(result)