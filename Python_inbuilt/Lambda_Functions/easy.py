# Square of a number:
# Create a lambda function that takes a number and returns its square.
#  i need to know about map, filter and reduce and functools as well add as the next topic.

square = lambda x: x * x

print(square(5))

# Check if a number is even:
# Create a lambda function that checks if a number is even.

is_even = lambda x: x % 2 == 0

print(is_even(4))

# Sum of two numbers:
# Create a lambda function that takes two numbers and returns their sum.

sum = lambda x, y: x + y

print(sum(5, 10))

# Convert temperature:
# Create a lambda function to convert Fahrenheit to Celsius.

convert_temp = lambda f: (f - 32) * 5 / 9

print(convert_temp(132))

# Filter odd numbers:
# Use a lambda function with filter() to get all odd numbers from a list.

numbers = [1, 2, 3, 4, 5]
odd_list = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_list)
