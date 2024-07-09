# **Generator Expressions**

Generator expressions are a concise way to create generators without using a full `def` function. They allow you to iterate over sequences and perform operations on the fly, making your code more memory efficient.

#### **Basics of Generator Expressions**

A generator expression looks similar to a list comprehension, but uses parentheses instead of square brackets. Here’s a basic example:

```python
# List comprehension
squares = [x * x for x in range(10)]

# Generator expression
squares_gen = (x * x for x in range(10))
```

The key difference is that `squares` is a list, whereas `squares_gen` is a generator.

#### **Examples and Exercises**

**Example 1: Basic Generator Expression**

Create a generator that yields the square of each number in a given list.

```python
numbers = [1, 2, 3, 4, 5]
squares_gen = (x * x for x in numbers)

# To get the values, you can use a for loop
for square in squares_gen:
    print(square)
```





**Exercise 4: Sum of Squares**

Write a function that takes a list of numbers and returns the sum of their squares using a generator expression.

```python
def sum_of_squares(numbers):
    # Write your generator expression and sum logic here
    return ...

numbers = [1, 2, 3, 4, 5]
print(sum_of_squares(numbers))
```
