# Given a matrix (list of lists), find the sum of all elements.
from functools import reduce

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculate the sum of all elements in the matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = reduce(lambda x,y: x+y, [x for sublist in matrix for x in sublist])
print(result)


# # Create a dictionary where the keys are tuples (name, age) and the values are occupations.
#
# people = {('Alice', 30): 'Engineer', ('Bob', 25): 'Doctor', ('Charlie', 35): 'Artist'}
#
# # Retrieve the occupation of 'Bob'

people = {('Alice', 30): 'Engineer', ('Bob', 25): 'Doctor', ('Charlie', 35): 'Artist'}

