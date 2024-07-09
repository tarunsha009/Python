# 1. all
# The all function returns True if all elements in an iterable are true (or if the iterable is empty).

numbers = [2, 4, 6, 8]
result = all(n % 2 == 0 for n in numbers)
print(result)  # Output: True

# 2. any
# The any function returns True if any element in an iterable is true. If the iterable is empty, it returns False.

numbers = [1, 3, 5, 8]
result = any(n % 2 == 0 for n in numbers)
print(result)  # Output: True


# 3. zip
# The zip function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables. It stops when the shortest input iterable is exhausted.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# Questions to Practice
# Check if All Elements are Positive:
# Write a function that checks if all numbers in a list are positive using all.

list1 = [-1,2,3,4,5]
result = all(n > 0 for n in list1)
print(result)


# Check if Any String is Empty:
# Write a function that checks if any string in a list of strings is empty using any.
words = ['hi', 'hello', 'world', 'yes', 'no', '']
result = any(len(i) == 0 for i in words)
print(result)


# Pair Elements:
# Write a function that pairs elements from two lists of equal length using zip.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)

# Combine Lists with Conditions:
# Write a function that combines two lists element-wise if both elements are positive using zip, all, and list comprehensions.

list1 = [1, -2, 3]
list2 = [4, -5, 6]

result = [(x, y) for x, y in zip(list1, list2) if x > 0 and y > 0]
print(result)

assert result == [(1, 4), (3, 6)]
