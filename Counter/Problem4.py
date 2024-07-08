# Write a function that takes two strings as input and returns True if they are anagrams of each other (contain the same letters with the same frequency).

# Input:
#
# str1 = "listen"
# str2 = "silent"
#
# Expected Output:
# True

from collections import Counter


def check_anagrams(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)

    return c1 == c2

str1 = "listen"
str2 = "silent"
print("Is anagram: ", check_anagrams(str1, str2))