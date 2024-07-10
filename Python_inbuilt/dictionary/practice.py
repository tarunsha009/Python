# Creating a dictionary with squares of numbers:
squares = {x: x**2 for x in range(6)}
print(squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Creating a dictionary from a list of tuples:
pairs = [("name", "John"), ("age", 30), ("city", "New York")]
my_dict = {key: value for key, value in pairs}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Filtering dictionary items:
original_dict = {"name": "John", "age": 30, "city": "New York", "email": "john@example.com"}
filtered_dict = {k: v for k, v in original_dict.items() if isinstance(v, int)}
print(filtered_dict)
# Output: {'age': 30}


# Create a dictionary from a list of strings with string lengths as values:
words = ["apple", "banana", "cherry"]
length = {x:len(x) for x in words}
print(length)

# Create a dictionary with numbers and their cubes:
numbers = range(1, 6)
cubes = {x: x **3 for x in numbers}

# Filter a dictionary to only keep items with values greater than a certain threshold:
scores = {"Alice": 85, "Bob": 75, "Charlie": 90, "David": 60}
output = {k:v for k, v in scores.items() if v > 65}
print(output)
