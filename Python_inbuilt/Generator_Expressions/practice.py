# **Exercise 1: Generator for Cubes**
#
# Write a generator expression that yields the cube of each number in a given list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

cubes_gen = (x **3 for x in numbers)

for cube in cubes_gen:
    print(cube)

# **Example 2: Filtering with Generator Expressions**
#
# Create a generator that yields only the even numbers from a given list.

numbers = [1, 2, 3, 4, 5]

cubes_gen = (x for x in numbers if x %2 == 0)

for cube in cubes_gen:
    print(cube)

# **Exercise 2: Filtering Odd Numbers**
#
# Write a generator expression that yields only the odd numbers from a given list.

numbers = [1, 2, 3, 4, 5]

cubes_gen = (x for x in numbers if x %2 != 0)

for cube in cubes_gen:
    print(cube)

# **Example 3: Using Generators with Functions**
#
# Create a generator that yields the lengths of strings in a list.

words = ['apple', 'banana', 'cherry', 'date']
lengths_gen = (len(word) for word in words)

for length in lengths_gen:
    print(length)

# **Exercise 3: Generators for Uppercased Strings**
#
# Write a generator expression that yields the uppercase version of each string in a list.

words = ['apple', 'banana', 'cherry', 'date']
uppercase_gen = (str(x).upper() for x in words)

for uppercased in uppercase_gen:
    print(uppercased)

# **Example 4: Using Generators in Functions**
#
# Define a function that takes a generator as an argument and prints its values.
def print_generator(gen):
    for value in gen:
        print(value)

numbers = [1, 2, 3, 4, 5]
squares_gen = (x * x for x in numbers)
print_generator(squares_gen)

# **Exercise 4: Sum of Squares**
#
# Write a function that takes a list of numbers and returns the sum of their squares using a generator expression.

def sum_of_squares(numbers):
    gen = (x **2 for x in numbers)

    return reduce(lambda x, y : x+y, gen)

numbers = [1, 2, 3, 4, 5]
print(sum_of_squares(numbers))