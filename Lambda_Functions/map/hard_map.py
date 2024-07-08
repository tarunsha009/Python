# Apply multiple functions:
# Given a list of numbers, apply two functions to each element: square the number and then double it.
# numbers = [1, 2, 3, 4]
# # Expected Output: [2, 8, 18, 32]

numbers = [1, 2, 3, 4]
result = list(map(lambda x: (x * x) * 2, numbers))
print(result)

# Custom transformation:
# Given a list of strings, transform each string by reversing it and then converting it to uppercase.
# words = ['hello', 'world', 'python']
# # Expected Output: ['OLLEH', 'DLROW', 'NOHTYP']

words = ['hello', 'world', 'python']

result = list(map(lambda x : str(x).upper()[::-1], words))
print(result)

# Flatten a list of lists:
# Given a list of lists of numbers, flatten it into a single list.
# list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# # Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

result = list(map(lambda x: x, [elem for sublist in list_of_lists for elem in sublist]))
print(result)