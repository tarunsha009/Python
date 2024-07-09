# Python’s itertools Module

The itertools module provides functions that create iterators for efficient looping. These functions can handle tasks such as generating permutations, combinations, and Cartesian products. Let’s explore the most common functions and their use cases.

Common Functions in itertools
1. count(start=0, step=1)
Creates an iterator that generates numbers starting from start and increments by step.

Example:
```python
import itertools

counter = itertools.count(start=5, step=3)
for num in counter:
    if num > 20:
        break
    print(num)
# Output: 5, 8, 11, 14, 17, 20

```

2. cycle(iterable)
Cycles through an iterable indefinitely.

Example:
```python
import itertools

cycler = itertools.cycle(['A', 'B', 'C'])
for _ in range(6):
    print(next(cycler))
# Output: A, B, C, A, B, C

```

3. repeat(object, times=None)
Repeats an object for a specified number of times.

Example:

```python
import itertools

repeater = itertools.repeat('Python', 3)
print(list(repeater))
# Output: ['Python', 'Python', 'Python']
```


4. permutations(iterable, r=None)
Generates all possible permutations of an iterable’s elements of length r.

Example:
```python
import itertools

perms = itertools.permutations([1, 2, 3], 2)
print(list(perms))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```


5. combinations(iterable, r)
Generates all possible combinations of an iterable’s elements of length r.

Example:

```python
import itertools

combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))
# Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

6. product(*iterables, repeat=1)
Computes the Cartesian product of input iterables.

Example:
```python
import itertools

prod = itertools.product([1, 2], ['A', 'B'])
print(list(prod))
# Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

7. combinations_with_replacement(iterable, r)
Generates all combinations of length r with replacement.

Example:

```python
import itertools

comb_wr = itertools.combinations_with_replacement([1, 2, 3], 2)
print(list(comb_wr))
# Output: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

8. chain(*iterables)
Chains multiple iterables into a single iterable.

Example:

```python
import itertools

chains = itertools.chain([1, 2, 3], ['A', 'B'])
print(list(chains))
# Output: [1, 2, 3, 'A', 'B']
```

9. islice(iterable, start, stop, step)
Slices an iterable from start to stop with a given step.

Example:

```python
import itertools

sliced = itertools.islice(range(10), 2, 8, 2)
print(list(sliced))
# Output: [2, 4, 6]
```

10. starmap(function, iterable)
Applies a function to arguments unpacked from tuples in an iterable.

Example:

```python
import itertools

pairs = [(2, 3), (4, 5), (6, 7)]
results = itertools.starmap(lambda x, y: x + y, pairs)
print(list(results))
# Output: [5, 9, 13]
```