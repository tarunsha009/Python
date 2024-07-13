### **`defaultdict` Overview**

#### **What is `defaultdict`?**

`defaultdict` is a subclass of the built-in `dict` class. It provides a default value for missing keys, eliminating the need for explicit checks and handling for missing keys.

**Syntax:**

```python
from collections import defaultdict

# Initialize defaultdict with a default factory function
my_dict = defaultdict(default_factory)
```

- **`default_factory`:** A function that returns the default value for new keys. Common options include `int`, `list`, and `set`.

#### **Why Use `defaultdict`?**

- **Simplifies Code:** Automatically handles missing keys and initializes them with a default value.
- **Common Use Cases:** Counting occurrences, grouping data, creating nested dictionaries.

#### **When to Use `defaultdict`?**

- When you want to avoid key errors and handle missing keys with a default value.
- Useful in scenarios where you perform frequent operations on dictionaries like counting, grouping, and organizing data.

### **`defaultdict` Examples**

#### **1. Basic Usage with `int`**

The `int` default factory initializes missing keys with `0`.

```python
from collections import defaultdict

# Initialize defaultdict with int, which defaults to 0
counter = defaultdict(int)

# Increment counts for characters
for char in "hello":
    counter[char] += 1

print(counter)  # Output: defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})
```

**Explanation:**
- Here, `defaultdict(int)` means any missing key will have a default value of `0`.

#### **2. Grouping Data with `list`**

The `list` default factory initializes missing keys with an empty list.

```python
from collections import defaultdict

# Initialize defaultdict with list
grouped_data = defaultdict(list)

# Group names by their first letter
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    grouped_data[name[0]].append(name)

print(grouped_data)  # Output: defaultdict(<class 'list'>, {'A': ['Alice'], 'B': ['Bob'], 'C': ['Charlie'], 'D': ['David'], 'E': ['Eve']})
```

**Explanation:**
- `defaultdict(list)` means any missing key will have a default value of an empty list.

#### **3. Creating a Nested Dictionary with `dict`**

The `dict` default factory initializes missing keys with an empty dictionary.

```python
from collections import defaultdict

# Initialize defaultdict with dict
nested_dict = defaultdict(dict)

# Set nested values
nested_dict['A']['a'] = 1
nested_dict['B']['b'] = 2

print(nested_dict)  # Output: defaultdict(<class 'dict'>, {'A': {'a': 1}, 'B': {'b': 2}})
```

**Explanation:**
- `defaultdict(dict)` means any missing key will have a default value of an empty dictionary.

### **Exercises for `defaultdict`**

#### **Exercise 1: Counting Words**

Write a function to count the frequency of each word in a list of strings.

```python
from collections import defaultdict

def count_words(words):
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count

# Test the function
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count_words(words))  # Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
```

#### **Exercise 2: Grouping Numbers**

Write a function to group a list of numbers by their parity (even or odd).

```python
from collections import defaultdict

def group_by_parity(numbers):
    parity_groups = defaultdict(list)
    for number in numbers:
        if number % 2 == 0:
            parity_groups['even'].append(number)
        else:
            parity_groups['odd'].append(number)
    return parity_groups

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
print(group_by_parity(numbers))  # Output: defaultdict(<class 'list'>, {'odd': [1, 3, 5], 'even': [2, 4, 6]})
```

#### **Exercise 3: Building a Nested Dictionary**

Write a function to build a nested dictionary where the keys are categories and the values are lists of items.

```python
from collections import defaultdict

def build_nested_dict(items):
    nested_dict = defaultdict(list)
    for category, item in items:
        nested_dict[category].append(item)
    return nested_dict

# Test the function
items = [("fruit", "apple"), ("vegetable", "carrot"), ("fruit", "banana"), ("vegetable", "broccoli")]
print(build_nested_dict(items))  # Output: defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'broccoli']})
```
