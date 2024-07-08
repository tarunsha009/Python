# Filter Function

The filter() function constructs an iterator from elements of an iterable for which a function returns true. Here's a detailed explanation and some practice problems

## Basic Usage of Filter
```python
# Syntax: filter(function, iterable)
# The function should return True or False.

# Example: Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

```