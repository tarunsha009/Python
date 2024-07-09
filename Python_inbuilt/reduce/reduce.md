# reduce in Python

reduce is a function from the functools module that applies a rolling computation to sequential pairs of values in a list

While not technically part of functools, it's often used in conjunction with it. reduce applies a function cumulatively to all items in an iterable, reducing it to a single value. functools provides a safe version of reduce called reduce (without the leading underscore).

### Syntax
````python
from functools import reduce

result = reduce(function, iterable[, initializer])

````

- function: a function of two arguments.
- iterable: an iterable to reduce.
- initializer (optional): starting value of the accumulator.

### Example
Summing a list of numbers:

````python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15

````

Finding the maximum value in a list:

````python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(max_result)  # Output: 5

````
Calculate the product of all numbers using reduce

````python
from functools import reduce

numbers = [1, 2, 3, 4]

# Calculate the product of all numbers using reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

````

## NOTE:

**reduce** works by taking two arguments and applying a function cumulatively to reduce a list to a single value. Meanwhile, **map** generally takes a single argument function and applies it to each element of an iterable independently. When map is used with multiple iterables, the function can take as many arguments as there are iterables.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_lists)  # Output: [5, 7, 9]

```