### Reverse Lookups

#### Introduction

Reverse lookups involve finding keys in a dictionary given a value. This can be useful when you need to retrieve the key(s) associated with a specific value. For this, we'll often use dictionary comprehensions to reverse the key-value pairs.

#### Example

Suppose you have a dictionary with student names as keys and their grades as values:

```python
grades = {
    'Alice': 'A',
    'Bob': 'B',
    'Charlie': 'A',
    'David': 'C'
}
```

You want to create a new dictionary where the keys are grades and the values are lists of students who received those grades.

#### Solution

To achieve this, you can use a dictionary comprehension combined with a loop to collect students for each grade:

```python
grades = {
    'Alice': 'A',
    'Bob': 'B',
    'Charlie': 'A',
    'David': 'C'
}

reverse_grades = {}
for student, grade in grades.items():
    if grade not in reverse_grades:
        reverse_grades[grade] = []
    reverse_grades[grade].append(student)

print(reverse_grades)
# Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}
```

Or more concisely using a dictionary comprehension:

```python
reverse_grades = {grade: [student for student, g in grades.items() if g == grade] for grade in set(grades.values())}
print(reverse_grades)
# Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}
```

Certainly! Let's break down the statement `merged_dict = {**dict1, **dict2}` and understand how it works.

### Unpacking Dictionaries with `**`

The `**` operator is used to unpack dictionaries in Python. When you use `**` before a dictionary, it unpacks its key-value pairs. Here's a more detailed explanation:

1. **Merging Dictionaries:**
   - When you use `{**dict1, **dict2}`, it creates a new dictionary and inserts all the key-value pairs from `dict1` and `dict2`.
   - If there are duplicate keys, the values from the latter dictionary (`dict2` in this case) will overwrite the values from the former dictionary (`dict1`).

   ```python
   dict1 = {'a': 1, 'b': 2}
   dict2 = {'b': 3, 'c': 4}
   merged_dict = {**dict1, **dict2}
   print(merged_dict)
   # Output: {'a': 1, 'b': 3, 'c': 4}
   ```

2. **Syntax and Usage:**
   - This syntax can only be used with dictionaries.
   - It is useful for merging dictionaries in a concise way.
   - This feature was introduced in Python 3.5.

3. **General Usage:**
   - You can use this technique whenever you need to combine multiple dictionaries.

### Example with Multiple Dictionaries

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5, 'e': 6}

merged_dict = {**dict1, **dict2, **dict3}
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
```


#### Using Dictionary Comprehension:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {k: v for d in (dict1, dict2) for k, v in d.items()}
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}
```

### Limitations

- The `**` operator for unpacking can only be used with dictionaries. It won't work with other data structures like lists, tuples, or sets.
- When merging dictionaries with `**`, if there are duplicate keys, the value from the last dictionary in the unpacking order will be used.

### Summary

- The `**` operator unpacks the key-value pairs of dictionaries.
- Useful for merging dictionaries in a concise way.
- Introduced in Python 3.5 and later versions.
- Only applicable to dictionaries.


Python provides similar unpacking capabilities for other data structures like lists, tuples, and sets. Here’s how you can use them:

### Lists and Tuples

You can use the `*` operator to unpack lists and tuples.

#### Merging Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = [*list1, *list2]
print(merged_list)
# Output: [1, 2, 3, 4, 5, 6]
```

#### Merging Tuples

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = (*tuple1, *tuple2)
print(merged_tuple)
# Output: (1, 2, 3, 4, 5, 6)
```

### Sets

You can use the `|` operator or the `update` method to merge sets. However, if you want to use unpacking, you can use the `*` operator within the `set` constructor.

#### Merging Sets

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using the | operator
merged_set = set1 | set2
print(merged_set)
# Output: {1, 2, 3, 4, 5}

# Using unpacking
merged_set = {*set1, *set2}
print(merged_set)
# Output: {1, 2, 3, 4, 5}
```

### General Guidelines

- **Lists and Tuples:** Use the `*` operator to unpack.
- **Sets:** Use the `*` operator within a set constructor or the `|` operator.
- **Dictionaries:** Use the `**` operator to unpack.

### Examples

#### Concatenating Multiple Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

merged_list = [*list1, *list2, *list3]
print(merged_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Concatenating Multiple Tuples

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)

merged_tuple = (*tuple1, *tuple2, *tuple3)
print(merged_tuple)
# Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

#### Concatenating Multiple Sets

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {7, 8, 9}

merged_set = {*set1, *set2, *set3}
print(merged_set)
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

### Summary

- **Lists and Tuples:** Use the `*` operator to unpack and concatenate them.
- **Sets:** Use the `*` operator within a set constructor or the `|` operator to merge sets.
- **Dictionaries:** Use the `**` operator to unpack and merge them.
