# 1. **Create an Iterator for a Range of Numbers**:
#    - Implement an iterator that generates numbers from a start value to an end value (inclusive).
#    - Expected Output: An iterable that produces numbers from start to end.

class MyIterator:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        else:
            self.current += 1
            return  self.current - 1


iter = MyIterator(1, 5)

for v in iter:
    print(v)


# 2. **Custom Iterator for Fibonacci Sequence**:
#    - Create an iterator that generates the Fibonacci sequence up to a specified number of elements.
#    - Expected Output: An iterable that produces the Fibonacci sequence.

class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.next_val = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        else:
            self.current, self.next_val = self.next_val, self.current + self.next_val
            self.count += 1
            return self.current

# Using the Fibonacci iterator
fib_iter = FibonacciIterator(10)
for num in fib_iter:
    print(num)  # Output: Fibonacci sequence up to 10 elements


# 3. **Chaining Iterators**:
#    - Use `itertools.chain` to chain multiple iterators and iterate over them as a single sequence.
#    - Input: Multiple iterables like `[1, 2, 3]` and `['a', 'b', 'c']`
#    - Expected Output: `[1, 2, 3, 'a', 'b', 'c']`

import itertools

iter1 = [1, 2, 3]
iter2 = ['a', 'b', 'c']

# Using itertools.chain to chain iterators
chained_iter = itertools.chain(iter1, iter2)
for item in chained_iter:
    print(item)  # Output: 1 2 3 a b c

