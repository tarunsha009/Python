# **Task:** Combine two lists such that the output contains only the elements from the first list if they are even, and from the second list if they are odd.
#
# **Input:** `list1 = [1, 2, 3, 4]`, `list2 = [5, 6, 7, 8]`
#
# **Expected Output:** `[5, 2, 7, 4]`

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = [a if a % 2 == 0 else b for a, b in zip(list1, list2)]
print(result)

# **Task:** Combine three lists such that the output contains the maximum element at each position from the three lists.
#
# **Input:** `list1 = [1, 4, 7]`, `list2 = [2, 5, 6]`, `list3 = [3, 8, 5]`
#
# **Expected Output:** `[3, 8, 7]`

list1 = [1, 4, 7]
list2 = [2, 5, 6]
list3 = [3, 8, 5]

result = [max(a, b, c) for a, b, c in zip(list1, list2, list3)]
print(result)

# **Task:** Combine two lists of equal length by adding corresponding elements.
#
# **Input:** `list1 = [1, 2, 3]`, `list2 = [4, 5, 6]`
#
# **Expected Output:** `[5, 7, 9]`

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = [a + b for a, b in zip(list1, list2)]
print(result)

# **Task:** Combine two lists such that the output contains elements from the first list if they are less than 5, and from the second list otherwise.
#
# **Input:** `list1 = [1, 6, 3, 8]`, `list2 = [5, 2, 7, 4]`
#
# **Expected Output:** `[1, 2, 3, 4]`

list1 = [1, 6, 3, 8]
list2 = [5, 2, 7, 4]

result = [a if a < 5 else b for a, b in zip(list1, list2)]
print(result)

# **Task:** Combine two lists using a custom function that multiplies elements from the two lists.
#
# **Input:** `list1 = [1, 2, 3]`, `list2 = [4, 5, 6]`
#
# **Expected Output:** `[4, 10, 18]`


list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = [a * b for a, b in zip(list1, list2)]
print(result)
