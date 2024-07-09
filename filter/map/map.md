# map()

The map() function applies a given function to all items in an input list (or any iterable) and returns a map object, which can then be converted into a list, tuple, etc.

## Syntax

```python
map(function, iterable)
```

- function: A function that takes a single argument and is applied to all elements of the iterable.
- iterable: A sequence (e.g., list, tuple) to which the function is applied.

## Example Problem: Double the numbers

### Task:
Use map to double all numbers in a list.

```python
numbers = [1, 2, 3, 4, 5]
# Expected Output: [2, 4, 6, 8, 10]
```

### Solution:
We need to apply a function that doubles each number in the list. A lambda function is perfect for this.

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
# Output: [2, 4, 6, 8, 10]
```

### Breakdown:

- lambda x: x * 2 is a lambda function that takes one argument x and returns x * 2.
- map(lambda x: x * 2, numbers) applies this lambda function to each element in the numbers list.
- list(map(...)) converts the map object into a list.