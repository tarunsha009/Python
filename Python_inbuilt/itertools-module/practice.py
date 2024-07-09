import itertools

# Counter example
counter = itertools.count(0, 5)
for i in counter:
    if i == 50:
        break
    print(i)

# chain example
fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "pea", "cucumber"]
combined_foods = itertools.chain(fruits, vegetables)

for item in combined_foods:
    print(item)

# cycle example

colors = ["red", "green", "blue"]
color_cycle = itertools.cycle(colors)
print("########## Cycle example ##########")
for i in range(10):
    print(next(color_cycle))

# zip example

letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]

# Zipping letters and numbers together
letter_number_pairs = zip(letters, numbers)

for pair in letter_number_pairs:
    print(pair)

# permutation example:
# Generates all possible permutations of an iterable’s elements of length r.
perm = itertools.permutations([1, 2, 3], 2)
print(list(perm))

# combinations example:
# Generates all possible combinations of an iterable’s elements of length r.

combination = itertools.combinations([1, 2, 3], 2)
print(list(combination))

# product example:

result = itertools.product([1, 2], ['A', 'B'])
print(list(result))
