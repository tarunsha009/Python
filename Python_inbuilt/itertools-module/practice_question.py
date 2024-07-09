# 1. Generate All Possible Two-Digit Numbers
# Generate all two-digit numbers using product.
import itertools

result = itertools.product(range(1, 10), repeat=2)
print(list(result))
two_digits = [''.join(map(str, num)) for num in itertools.product(range(1, 10), repeat=2)]
print(two_digits)


# 3. Generate All Subsets of a Set
# Generate all subsets of a set (power set).
abc = itertools.chain.from_iterable(itertools.combinations([1,2,3], r) for r in range(4))
print(list(abc))


# You are given a string .
# Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

max_size = 2
# s = ''.join(sorted("HACK"))
s = [1, 2, 3, 4]
for size in range(1, max_size + 1):
    for comb in itertools.combinations(s, size):
        print(comb)
        # print(''.join(str(comb)))