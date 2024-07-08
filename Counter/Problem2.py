# Problem 2:
# Write a function that takes two lists as input and returns True if they contain the same elements (with the same frequency), regardless of the order.

# Input:
# list1 = [1, 2, 2, 3, 4]
# list2 = [2, 1, 3, 2, 4]

# Expected Output: True

from collections import Counter


def check_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)

    return c1 == c2

list1 = [1, 2, 2, 3, 4]
list2 = [2, 1, 3, 2, 4]
print(check_elements(list1, list2))