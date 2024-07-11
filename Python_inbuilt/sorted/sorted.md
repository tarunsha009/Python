The `sorted()` function in Python is very versatile and can be used with different data structures and scenarios. Here are some common use cases and examples:

### Sorting a List of Tuples

#### By Second Element

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)
# Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
```

#### By First Element in Descending Order

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_list = sorted(tuples_list, key=lambda x: x[0], reverse=True)
print(sorted_list)
# Output: [(3, 'apple'), (2, 'cherry'), (1, 'banana')]
```

### Sorting a Dictionary

#### By Keys

```python
dict_ = {'b': 1, 'a': 2, 'c': 3}
sorted_by_keys = dict(sorted(dict_.items()))
print(sorted_by_keys)
# Output: {'a': 2, 'b': 1, 'c': 3}
```

#### By Values

```python
dict_ = {'b': 1, 'a': 2, 'c': 3}
sorted_by_values = dict(sorted(dict_.items(), key=lambda item: item[1]))
print(sorted_by_values)
# Output: {'b': 1, 'a': 2, 'c': 3}
```

### Sorting a List of Dictionaries

#### By a Specific Key in Each Dictionary

```python
list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}, {'name': 'Doe', 'age': 30}]
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
print(sorted_list)
# Output: [{'name': 'Jane', 'age': 22}, {'name': 'John', 'age': 25}, {'name': 'Doe', 'age': 30}]
```

### Sorting a String

```python
string = "hello"
sorted_string = ''.join(sorted(string))
print(sorted_string)
# Output: 'ehllo'
```

### Sorting a List of Strings

#### Alphabetically

```python
strings_list = ["banana", "apple", "cherry"]
sorted_list = sorted(strings_list)
print(sorted_list)
# Output: ['apple', 'banana', 'cherry']
```

#### By Length of Strings

```python
strings_list = ["banana", "apple", "cherry"]
sorted_list = sorted(strings_list, key=len)
print(sorted_list)
# Output: ['apple', 'banana', 'cherry']
```

### Sorting a Set

```python
set_ = {3, 1, 2}
sorted_set = sorted(set_)
print(sorted_set)
# Output: [1, 2, 3]
```

### Sorting with Custom Functions

You can define custom functions for more complex sorting logic.

#### Custom Function Example

```python
def custom_sort(t):
    return t[1]

tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_list = sorted(tuples_list, key=custom_sort)
print(sorted_list)
# Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### Summary

- **Lists:** `sorted()` can sort lists of any elements, using a custom key function if needed.
- **Dictionaries:** `sorted()` can be used to sort dictionaries by keys or values by converting the dictionary items to a list of tuples.
- **Strings:** `sorted()` can sort the characters in a string.
- **Sets:** `sorted()` can sort elements of a set by converting it to a list.

The `sorted()` function is flexible and powerful, allowing you to define the criteria by which you want to sort your data using the `key` parameter. You can sort in ascending or descending order using the `reverse` parameter.
