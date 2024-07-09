### **Lists and Tuples**

---

## **1. Lists**

### **Basic Operations**

**1. List Creation:**
```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
```

**2. Indexing and Slicing:**
```python
# Indexing
print(my_list[0])   # Output: 1

# Slicing
print(my_list[1:4]) # Output: [2, 3, 4]
```

**3. Common Methods:**
```python
# Append
my_list.append(6)  # Adds 6 to the end of the list

# Extend
my_list.extend([7, 8])  # Adds [7, 8] to the end of the list

# Insert
my_list.insert(2, 10)  # Inserts 10 at index 2

# Remove
my_list.remove(10)  # Removes the first occurrence of 10

# Pop
my_list.pop()  # Removes and returns the last item

# Count
my_list.count(4)  # Counts occurrences of 4 in the list

# Index
my_list.index(5)  # Finds the index of the first occurrence of 5

# Sorting
my_list.sort()  # Sorts the list in place

# Reversing
my_list.reverse()  # Reverses the list in place
```

### **Advanced Techniques**

**1. List Comprehensions:**
```python
# Basic List Comprehension
squares = [x**2 for x in my_list]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64]

# Conditional List Comprehension
even_squares = [x**2 for x in my_list if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64]
```

**2. Nested Lists:**
```python
# Creating Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0][1])  # Output: 2

# List Comprehension with Nested Lists
flattened = [item for sublist in matrix for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**3. List Operations:**
```python
# Combining Lists
combined_list = my_list + [10, 11, 12]

# Repeating Lists
repeated_list = my_list * 2
```

---

### **Exercise: Lists**

**1. Basic Operations Exercise:**
```python
# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Perform the following tasks:
# a. Add a number 11 to the end of the list
# b. Extend the list with numbers 12 and 13
# c. Insert the number 0 at the beginning of the list
# d. Remove the number 5 from the list
# e. Find the index of the number 8
# f. Sort the list in descending order
# g. Reverse the list

# Your code here:
```

**2. List Comprehensions Exercise:**
```python
# Given a list of integers, create a new list with the squares of the odd numbers only.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use list comprehension to create a new list
# Your code here:
```

**3. Nested Lists Exercise:**
```python
# Given a matrix (list of lists), find the sum of all elements.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculate the sum of all elements in the matrix
# Your code here:
```

---
