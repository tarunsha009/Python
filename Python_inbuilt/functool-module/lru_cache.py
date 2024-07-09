# 1. Fibonacci Sequence
# Task: Use lru_cache to optimize the calculation of Fibonacci numbers.
#
# What you need to do:
#
# Define a recursive fibonacci(n) function.
# Add @lru_cache to cache the results.
# Compute Fibonacci of 30.

from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n ==0 or n ==1:
        return 0
    if n ==2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


# 2. Factorial Calculation
# Task: Use lru_cache to optimize the calculation of factorial numbers.
#
# What you need to do:
#
# Define a recursive factorial(n) function.
# Add @lru_cache to cache the results.
# Compute the factorial of 10.

@lru_cache(maxsize=128)
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print(factorial(5))


# 3. Memoization for Recursive Sum
# Task: Create a recursive function to compute the sum of integers up to n, and optimize it with lru_cache.
#
# What you need to do:
#
# Define a recursive sum_up_to(n) function.
# Add @lru_cache to cache the results.
# Compute the sum up to 50.

@lru_cache(maxsize=128)
def sum_up_to(n):
    if n <=0:
        return 0

    return n + sum_up_to(n -1)

print(sum_up_to(50))
