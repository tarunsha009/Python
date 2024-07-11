# ### Exercise: Practice Problems
#
# 1. **Sorting Tuples:**
#    - Sort a list of tuples by the second element in descending order.
#    - Input: `[(3, 'apple'), (1, 'banana'), (2, 'cherry')]`
#    - Expected Output: `[(2, 'cherry'), (1, 'banana'), (3, 'apple')]`

value = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
# sorted_value = [t in sorted(value, key: value[][])]
print([t for t in sorted(value, key= lambda x : x[1], reverse=True)])


# 2. **Filtering Tuples:**
#    - Filter tuples where the second element starts with the letter 'a'.
#    - Input: `[(3, 'apple'), (1, 'banana'), (2, 'apricot')]`
#    - Expected Output: `[(3, 'apple'), (2, 'apricot')]`

value = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
print(list(filter(lambda x : str(x[1]).startswith('a'), value)))

# 3. **Transforming Tuples:**
#    - Convert the first element of each tuple to its square.
#    - Input: `[(3, 'apple'), (1, 'banana'), (2, 'cherry')]`
#    - Expected Output: `[(9, 'apple'), (1, 'banana'), (4, 'cherry')]`
value = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
print([(t[0] **2, t[1]) for t in value])

# 4. **Nested Tuples:**
#    - Create a list of tuples where each tuple contains a number and a tuple with the square and cube of that number.
#    - Input: `[1, 2, 3]`
#    - Expected Output: `[(1, (1, 1)), (2, (4, 8)), (3, (9, 27))]`
value = [1, 2, 3]
print([(t, (t **2, t **3)) for t in value])