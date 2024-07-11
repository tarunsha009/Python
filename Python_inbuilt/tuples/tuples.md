### Understanding Tuples and Lists of Tuples

#### What is a Tuple?

A tuple is an immutable sequence type in Python, meaning once it is created, it cannot be modified. Tuples are defined by enclosing the elements in parentheses `()`.

**Example:**

```python
my_tuple = (1, 'apple', 3.5)
print(my_tuple)
# Output: (1, 'apple', 3.5)
```

- Tuples can contain elements of different data types.
- You can access elements in a tuple using indexing, just like lists.

**Accessing Elements:**

```python
print(my_tuple[0])
# Output: 1

print(my_tuple[1])
# Output: 'apple'
```

#### List of Tuples

A list of tuples is a list where each element is a tuple. This structure is useful for representing collections of related data.

**Example:**

```python
list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
print(list_of_tuples)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
```

- Each element in the list is a tuple.
- You can perform operations on this list, such as sorting, filtering, and transforming the data within the tuples.

#### Operations on List of Tuples

### Activity 1: Sorting a List of Tuples

**Example 1: Sort by First Element**

Given a list of tuples, sort them based on the first element.

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_by_first = sorted(tuples_list)
print(sorted_by_first)
# Output: [(1, 'banana'), (2, 'cherry'), (3, 'apple')]
```

**Example 2: Sort by Second Element**

To sort the list of tuples by the second element, we use the `key` parameter in the `sorted()` function.

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
sorted_by_second = sorted(tuples_list, key=lambda x: x[1])
print(sorted_by_second)
# Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### Activity 2: Filtering a List of Tuples

**Example: Filter Tuples Based on a Condition**

Filter the list of tuples to keep only those tuples where the first element is greater than 1.

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
filtered_tuples = [t for t in tuples_list if t[0] > 1]
print(filtered_tuples)
# Output: [(3, 'apple'), (2, 'cherry')]
```

### Activity 3: Transforming a List of Tuples

**Example: Add a Value to Each Tuple**

Add 1 to the first element of each tuple in the list.

```python
tuples_list = [(3, 'apple'), (1, 'banana'), (2, 'cherry')]
transformed_tuples = [(t[0] + 1, t[1]) for t in tuples_list]
print(transformed_tuples)
# Output: [(4, 'apple'), (2, 'banana'), (3, 'cherry')]
```

### Activity 4: Nested Tuple Manipulation

Sometimes, tuples can be nested within other tuples or lists. Manipulating such structures requires a good understanding of how to access and modify the nested elements.

**Example: Accessing Nested Tuples**

```python
nested_tuples = [(1, (2, 'apple')), (3, (4, 'banana'))]
# Access the second element of the first tuple
nested_value = nested_tuples[0][1]
print(nested_value)
# Output: (2, 'apple')

# Access the string 'apple'
apple = nested_tuples[0][1][1]
print(apple)
# Output: 'apple'
```
