# Convert to uppercase:
# Convert all strings in a list to uppercase.
# words = ['hello', 'world', 'python']
# Expected Output: ['HELLO', 'WORLD', 'PYTHON']


words = ['hello', 'world', 'python']

upper_Case = list(map(lambda x: str(x).upper(), words))

print(upper_Case)

# Square the numbers:
# Square each number in a list.
# numbers = [1, 2, 3, 4, 5]
# # Expected Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x*x, numbers))
print(square)

