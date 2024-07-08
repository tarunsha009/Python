# List comprehensions

List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause, and then zero or more for or if clauses. The expressions can be anything, meaning you can put all kinds of objects in lists.

### Basic syntax:

```python
# Syntax: [expression for item in iterable if condition]

# Example: Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)
# Output: [1, 4, 9, 16, 25]

```