A custom sort function in Python allows you to define your own criteria for sorting. This is done by providing a key function to the `sorted()` function or the `sort()` method. The key function is called on each element of the iterable, and the return value of this function is used to determine the order of the elements.

Here's how the custom sort function works in detail:

### Basic Concept

When you use `sorted()` or `list.sort()`, you can pass a `key` parameter, which should be a function. This function takes one argument (an element from the list) and returns a value that will be used for sorting.

### Example: Sorting Tuples by Second Element

Let's break down the example provided earlier:

#### Data

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
```

#### Custom Sort Function

```python
def custom_sort(t):
    return t[1]
```

This function takes a tuple `t` as input and returns its second element (`t[1]`), which is a string (the fruit name in this case).

#### Sorting with the Custom Function

```python
sorted_list = sorted(tuples_list, key=custom_sort)
```

Here, `sorted()` will use the `custom_sort` function to sort `tuples_list`. For each tuple in `tuples_list`, the `custom_sort` function will be called, and the second element of each tuple will be used to determine the order.

#### Result

```python
print(sorted_list)
# Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
```

The tuples are sorted based on the alphabetical order of their second elements.

### Using Lambda for Custom Sort

Instead of defining a separate function, you can use a lambda function for concise inline key functions.

```python
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)
# Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### Other Examples

#### Sorting by Multiple Criteria

You can sort by multiple criteria by returning a tuple from the key function.

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry'), (1, 'apple')]
sorted_list = sorted(tuples_list, key=lambda x: (x[0], x[1]))
print(sorted_list)
# Output: [(1, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'apple')]
```

This sorts primarily by the first element, and then by the second element in case of ties.

#### Sorting by Length of Strings in a List

```python
strings_list = ["banana", "apple", "cherry"]
sorted_list = sorted(strings_list, key=len)
print(sorted_list)
# Output: ['apple', 'banana', 'cherry']
```

### Summary

- **Custom Sort Function:** A function you define that returns the value to be used for sorting.
- **Key Parameter:** The function passed to the `key` parameter of `sorted()` or `sort()`.
- **Lambda Function:** A concise way to write simple key functions inline.
