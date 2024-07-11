# Example 1: Sorting a List of Dictionaries
# Task
# Sort a list of dictionaries by a specified key.
# people = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Jane', 'age': 22},
#     {'name': 'Dave', 'age': 30}
# ]
# Expected Output:
# [
#     {'name': 'Jane', 'age': 22},
#     {'name': 'John', 'age': 25},
#     {'name': 'Dave', 'age': 30}
# ]

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 22},
    {'name': 'Dave', 'age': 30}
]

result = sorted(people, key= lambda x: x['age'])
print(result)

# Sorting a List of Tuples by Multiple Criteria
# Task
# Sort a list of tuples first by the second element in ascending order and then by the first element in descending order if the second elements are the same.
# items = [
#     (2, 'banana'),
#     (3, 'apple'),
#     (1, 'banana'),
#     (2, 'apple')
# ]
# Output:
# [
#     (2, 'apple'),
#     (3, 'apple'),
#     (1, 'banana'),
#     (2, 'banana')
# ]
items = [
    (2, 'banana'),
    (3, 'apple'),
    (1, 'banana'),
    (2, 'apple')
]

result = sorted(items, key= lambda t: (t[1], t[0]))
print(result)



