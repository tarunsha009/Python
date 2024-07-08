# Filter even numbers and square them:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [i ** 2 for i in numbers if i % 2 == 0]
print(result)


# Convert a list of strings to uppercase:
# words = ['hello', 'world', 'python']
# Expected Output: ['HELLO', 'WORLD', 'PYTHON']
words = ['hello', 'world', 'python']
result = [str(x).upper() for x in words]
print(result)

# Extract the first letter of each word:
# words = ['hello', 'world', 'python']
# # Expected Output: ['h', 'w', 'p']
words = ['hello', 'world', 'python']

result = [ str(x)[0] for x in words]
print(result)

# Generate a list of tuples (number, square):
# numbers = [1, 2, 3, 4, 5]
# Expected Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
numbers = [1, 2, 3, 4, 5]

result = [(x, x **2) for x in numbers]
print(result)

# Flatten a nested list:
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

result = [x for sublist in nested_list for x in sublist]
print(result)

# Multiply each number by 2:
# numbers = [1, 2, 3, 4, 5]
# # Expected Output: [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5]
print([ x * 2 for x in numbers])

# Create a list of even numbers up to 20:
# # Expected Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

result = [x for x in range(1, 21) if x % 2 == 0]
print(result)

# Convert a list of numbers to strings:
# numbers = [1, 2, 3, 4, 5]
# # Expected Output: ['1', '2', '3', '4', '5']

print([str(x) for x in numbers])


# Filter numbers greater than 5 and square them:
# numbers = [1, 2, 3, 6, 7, 8]
# # Expected Output: [36, 49, 64]

numbers = [1, 2, 3, 6, 7, 8]
result = [x **2 for x in numbers if x > 5]
print(result)

# Combine two lists element-wise into tuples:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Expected Output: [(1, 4), (2, 5), (3, 6)]
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = [ (list1[i], list2[i]) for i in range(len(list1))]
print(result)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [(x, y) for x, y in zip(list1, list2)]
print(combined)

# Create a list of tuples (index, value) for each element:
# words = ['hello', 'world', 'python']
# Expected Output: [(0, 'hello'), (1, 'world'), (2, 'python')]
words = ['hello', 'world', 'python']

result = [ (i, words[i]) for i in range(len(words))]
print(result)

words = ['hello', 'world', 'python']
indexed_words = [(i, word) for i, word in enumerate(words)]
print(indexed_words)


# Flatten a list of lists using list comprehension:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8]]
# # Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

result = [ item for sublist in nested_list for item in sublist]
print(result)

