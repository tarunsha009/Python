# Functools
The functools module in Python provides higher-order functions that operate on or return other functions. 

In Python's world, the functools module comes to the rescue when you're dealing with functions in a more advanced way. It provides a toolbox for working with functions as objects themselves, allowing you to modify their behavior or create new functions from them.

### Here's the gist of what functools offers:

**Higher-order functions:** These are functions that take functions as arguments or return functions as results. functools equips you with tools to create and manipulate higher-order functions.

**Common function** few important functions from functools:

- functools.reduce(): You've already used this to reduce a list to a single value.
- functools.partial(): Allows you to fix a certain number of arguments of a function and generate a new function.
- functools.lru_cache(): Provides a decorator to cache the results of a function to improve performance.


## 1. functools.partial()
functools.partial() allows you to "freeze" some portion of a function's arguments and/or keywords resulting in a new function with fewer arguments.

functools.partial allows you to fix a certain number of arguments of a function and generate a new function. This can be very useful when you have a function that you frequently call with some arguments set to the same values.

- **`partial(func, *args, **kwargs):`** This function creates a new function by fixing a subset of arguments of the original function (func). The remaining arguments are left open for future calls. Imagine partially filling out a form – partial does the same for functions, fixing some values beforehand.

```python
from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that multiplies any number by 2
double = partial(multiply, 2)

print(double(5))  # Output: 10


def greet(name, time_of_day):
  return f"Good {time_of_day}, {name}!"

# Create a new function 'good_morning' pre-filling the time_of_day argument
good_morning = partial(greet, time_of_day="morning")

print(good_morning("Alice"))  # Output: Good morning, Alice!


```

## 2. functools.lru_cache()
functools.lru_cache() is used for memoization to cache the results of expensive function calls and reuse them when the same inputs occur again.

### Basic Concepts
**What It Does:** It stores the results of function calls based on the arguments. If the function is called again with the same arguments, it returns the cached result instead of recomputing it.
LRU: Stands for “Least Recently Used”. The cache will hold only a certain number of results, and the least recently used results are discarded when the cache exceeds this limit.

#### Syntax:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def function(args):
    # Function body

```
- maxsize: The maximum number of items to cache. If set to None, the cache can grow without bound.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
print(factorial(6))  # Output: 720 (uses cached value of factorial(5))

```