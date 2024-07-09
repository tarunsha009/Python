from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that multiplies any number by 2
double = partial(multiply, 2)

print(double(5))  # Output: 10


# Partial Function for Greeting:
# Create a partial function that greets a person with a specific greeting message.
# Task: Define a function greet(name, greeting) that returns a greeting message. Create a partial function that always greets with "Hello".

def greet(name, greeting):
    return f" {greeting}, {name}"

partial_method = partial(greet, greeting = "Hello")

print(partial_method("tarun"))

# 2. Formatting Strings
# Task: Define a function format_string(string, prefix, suffix) that adds a prefix and suffix to a string. Create a partial function that adds the prefix "Mr." and suffix "esq" to a name.

def format_string(string, prefix, suffix):
    return f"{prefix} {string} {suffix}"

partial_method = partial(format_string, prefix = 'Mr.', suffix = 'esq')

print(partial_method("tarun"))


# 3. Filtering with a Minimum Value
# Task: Define a function filter_by_min(value, min_value) that returns True if value is greater than min_value. Create a partial function that uses a minimum value of 10.

def filter_by_min(value, min_value):
    return value > min_value

min_ten = partial(filter_by_min, min_value = 10)

print(min_ten(15))


