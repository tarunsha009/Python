
# Problem 1:
# Write a function that takes a string as input and returns the frequency of each character in the string using a Counter.
# Input:
# string = "hello"
# Expected Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}


from collections import Counter


def frequency(str):
    counter = Counter(str)
    for key, value in counter.items():
        print(key, value)
    # return counter

frequency("Hello")
# print(frequency("Hello"))

