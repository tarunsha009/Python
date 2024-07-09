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