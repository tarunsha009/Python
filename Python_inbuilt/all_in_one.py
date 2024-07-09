# Problem 1: Filter and Transform
# Given a list of numbers, filter out the even numbers, square the remaining odd numbers, and then sum them.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: 165
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = reduce(lambda x, y : x+ y, map(lambda x: x **2, filter(lambda x: x % 2 !=0,numbers )))

print(sum)


# Problem 2: Concatenate Strings
# Given a list of strings, concatenate the strings that start with a vowel and then return the length of the resulting string.

# words = ["apple", "banana", "orange", "umbrella", "kiwi"]
# # Expected Output: 20

words = ["apple", "banana", "orange", "umbrella", "kiwi"]

print(reduce(lambda x, y : x + y, map(lambda x: len(x), filter(lambda x: str(x)[0] in 'aeiou', words))))

# Problem 3: Flatten and Sum
# Given a list of lists of integers, flatten the list, filter out the even numbers, and then return the sum of the remaining numbers.
# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Expected Output: 25

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output = reduce(lambda x, y : x+y , filter(lambda x : x % 2 != 0, [item for sublist in lists for item in sublist]))

print(output)


# Problem 4: Extract and Transform
# Given a list of strings, extract the first letter of each string, convert it to uppercase, and then join them into a single string.
# words = ["hello", "world", "python"]
# # Expected Output: "HWP"

words = ["hello", "world", "python"]

output = reduce(lambda x , y: x+y, map(lambda x: str(x)[0].upper(), words))
print(output)


# Problem 5: Transform and Filter
# Given a list of numbers, double each number, filter out those greater than 10, and then find the product of the remaining numbers.
# Example:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Expected Output: 3840

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([item * 2 for item in numbers])
# print(list(filter(lambda x : x >= 10, [item * 2 for item in numbers])))

output = reduce(lambda x ,y: x *y, filter(lambda x : x <= 10, [item * 2 for item in numbers]))
print(output)


# Combined Exercise
# Challenge: Given a list of dictionaries representing students, filter out students with a grade below 50, convert the remaining students' names to uppercase, extract their names, and then concatenate the names into a single string.

# students = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 45},
#     {"name": "Charlie", "grade": 60},
#     {"name": "David", "grade": 30},
#     {"name": "Eve", "grade": 90}
# ]
# # Expected Output: "ALICECHARLIEEVE"
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 45},
    {"name": "Charlie", "grade": 60},
    {"name": "David", "grade": 30},
    {"name": "Eve", "grade": 90}
]

filter_student = list(filter(lambda x: x['grade'] > 50, students))
upper_case = reduce(lambda x, y: x+y, map(lambda x: str(x['name']).upper(), filter_student))
print(upper_case)



# Problem: Given a list of dictionaries representing students, filter out students with grades below a specified threshold, square their grades, and then sum the squared grades.

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 45},
    {"name": "Charlie", "grade": 60},
    {"name": "David", "grade": 30},
    {"name": "Eve", "grade": 90}
]

# Filter students with grades above a threshold (e.g., 50)
# Square the grades of the remaining students
# Sum the squared grades

# Expected Output: Sum of squared grades for Alice, Charlie, and Eve
# Output should be 85^2 + 60^2 + 90^2 = 7225 + 3600 + 8100 = 18925

filter_student = list(filter(lambda x: x['grade'] > 50, students))
sum = reduce(lambda x, y: x+y, map(lambda x: x['grade'] ** 2, filter_student))
print(sum)



# Final Challenge:
# Problem: Given a list of dictionaries representing students, perform the following steps:
#
# Filter out students with grades below a specified threshold (e.g., 50).
# Square the grades of the remaining students.
# Filter out the squared grades that are below a certain value (e.g., 2000).
# Sum the remaining squared grades.
# Return the result.
# students = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 45},
#     {"name": "Charlie", "grade": 60},
#     {"name": "David", "grade": 30},
#     {"name": "Eve", "grade": 90}
# ]

# Steps:
# 1. Filter students with grades above 50
# 2. Square the grades of the remaining students
# 3. Filter out the squared grades that are below 2000
# 4. Sum the remaining squared grades
# 5. Return the result

# Expected Output: Sum of squared grades for Alice and Eve (since Charlie's squared grade is 3600 which is filtered out)
# Output should be 85^2 + 90^2 = 7225 + 8100 = 15325

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 45},
    {"name": "Charlie", "grade": 60},
    {"name": "David", "grade": 30},
    {"name": "Eve", "grade": 90}
]

filter_student = list(filter(lambda x: x['grade'] > 50, students))
sum = reduce(lambda x, y: x+y, filter(lambda x: x> 2000 ,map(lambda x: x['grade'] ** 2, filter_student)))
print(sum)

