# Extract first letter:
# Extract the first letter of each word in a list.
# words = ['hello', 'world', 'python']
# Expected Output: ['h', 'w', 'p']

words = ['hello', 'world', 'python']
first_letters = list(map(lambda x: str(x)[0], words))

print(first_letters)

# Sum corresponding elements:
# Given two lists of numbers, sum the corresponding elements of the lists.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# # Expected Output: [5, 7, 9]

list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum = list(map(lambda x, y: x + y, list1, list2))
print(sum)

# Concatenate corresponding elements:
# Given two lists of strings, concatenate the corresponding elements.
# list1 = ['hello', 'world']
# list2 = ['python', 'rocks']
# Expected Output: ['hellopython', 'worldrocks']

list1 = ['hello', 'world']
list2 = ['python', 'rocks']

result = list(map(lambda x, y: str(x) + str(y), list1, list2))
print(result)

# Find lengths of strings:
# Given a list of strings, find the length of each string.
# words = ['hello', 'world', 'python']
# Expected Output: [5, 5, 6]
words = ['hello', 'world', 'python']
result = list(map(lambda x: len(str(x)), words))
print(result)

# Conditional transformation:
# Given a list of numbers, if the number is even, double it; if odd, triple it.
# numbers = [1, 2, 3, 4, 5]
# Expected Output: [3, 4, 9, 8, 15]
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, numbers))

print(result)
