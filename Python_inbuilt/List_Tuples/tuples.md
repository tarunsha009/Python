## **Tuples**

### **Basic Operations**

**1. Tuple Creation:**
```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
```

**2. Indexing and Unpacking:**
```python
# Indexing
print(my_tuple[0])  # Output: 1

# Unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5
```

**3. Common Methods:**
```python
# Count
my_tuple.count(2)  # Counts occurrences of 2 in the tuple

# Index
my_tuple.index(4)  # Finds the index of the first occurrence of 4
```

### **Advanced Techniques**

**1. Tuple Operations:**
```python
# Combining Tuples
combined_tuple = my_tuple + (6, 7, 8)

# Repeating Tuples
repeated_tuple = my_tuple * 2
```

**2. Tuples as Dictionary Keys:**
```python
# Using Tuples as Keys in a Dictionary
my_dict = {('a', 1): 'value1', ('b', 2): 'value2'}
print(my_dict[('a', 1)])  # Output: 'value1'
```

### **Exercise: Tuples**

**1. Basic Operations Exercise:**
```python
# Create a tuple with elements from 1 to 5
my_tuple = (1, 2, 3, 4, 5)

# Perform the following tasks:
# a. Count the occurrences of the number 3
# b. Find the index of the number 4

# Your code here:
```

**2. Tuples as Dictionary Keys Exercise:**
```python
# Create a dictionary where the keys are tuples (name, age) and the values are occupations.

people = {('Alice', 30): 'Engineer', ('Bob', 25): 'Doctor', ('Charlie', 35): 'Artist'}

# Retrieve the occupation of 'Bob'
# Your code here:
```

---
