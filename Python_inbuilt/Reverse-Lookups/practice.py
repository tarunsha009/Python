# 1. **Finding Keys by Value:**
#    - Given a dictionary, create a function that returns a list of keys associated with a given value.
#    - Input: `{'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}`, value `2`
#    - Expected Output: `['b', 'd']`
dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
value = 2

result = [key for key, val in dict.items() if val == value]
print(result)

# 2. **Reversing a Dictionary:**
#    - Write a function that takes a dictionary and returns a new dictionary with keys and values swapped.
#    - Input: `{'a': 1, 'b': 2, 'c': 3}`
#    - Expected Output: `{1: 'a', 2: 'b', 3: 'c'}`
dict ={'a': 1, 'b': 2, 'c': 3}

result = {value : key for key, value in dict.items()}
print(result)


# 3. **Grouping by Value:**
#    - Given a dictionary, create a new dictionary where the keys are the unique values from the original dictionary and the values are lists of keys that had those values.
#    - Input: `{'Alice': 'A', 'Bob': 'B', 'Charlie': 'A', 'David': 'C'}`
#    - Expected Output: `{'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}`
dict = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A', 'David': 'C'}

result = {value : [k for k ,v in dict.items() if v == value ]for key, value in dict.items()}
print(result)

# Inverting a Dictionary with Lists:
#
# Given a dictionary where values are lists, invert the dictionary to create a new dictionary where each list item is a key and the original key is its value.
# Input: {'a': [1, 2], 'b': [3, 4]}
# Expected Output: {1: 'a', 2: 'a', 3: 'b', 4: 'b'}

dict = {'a': [1, 2], 'b': [3, 4]}
print({x: k for k, v in dict.items() for x in v})


# Finding Common Keys:
#
# Find the keys that are common to two dictionaries.
# Input: {'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 4, 'd': 5}
# Expected Output: ['b', 'c']

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

print([k for k in dict1.keys() for k2 in dict2.keys() if k == k2])

### Merging Dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

### Finding Common Keys:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

common_keys = [k for k in dict1.keys() if k in dict2.keys()]
print(common_keys)

### Summing Values by Key:
dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'c': 6}]

summed_values = {}
for d in dicts:
    for k, v in d.items():
        if k in summed_values:
            summed_values[k] += v
        else:
            summed_values[k] = v

print(summed_values)

### Combining Values for Common Keys:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(combined_dict)

### Inverting a Dictionary with Lists:
dict_with_lists = {'a': [1, 2], 'b': [3, 4]}

inverted_dict = {x: k for k, v in dict_with_lists.items() for x in v}
print(inverted_dict)





