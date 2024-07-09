# Filter out odd numbers:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)

# Filter strings with length greater than 3:
# words = ['hi', 'hello', 'world', 'yes', 'no']
# # Expected Output: ['hello', 'world']

words = ['hi', 'hello', 'world', 'yes', 'no']
result = list(filter(lambda x: len(x) > 3, words))
print(result)

# Filter prime numbers:
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [2, 3, 5, 7]
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# # Use this function in filter()
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_number = list(filter(is_prime, numbers))
print(prime_number)


# Filter palindromes:
# words = ['level', 'world', 'radar', 'python', 'civic']
# # Expected Output: ['level', 'radar', 'civic']

words = ['level', 'world', 'radar', 'python', 'civic']
def is_palindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

result = list(filter(is_palindrome, words))
print(result)

words = ['level', 'world', 'radar', 'python', 'civic']
palindromes = list(filter(lambda x: x == x[::-1], words))
print(palindromes)

# Filter multiples of a given number:
# numbers = [10, 20, 33, 40, 55, 60]
# multiple_of = 10
# # Expected Output: [10, 20, 40, 60]
numbers = [10, 20, 33, 40, 55, 60]

result = list(filter(lambda x: x % 10 == 0, numbers))
print(result)

# Filter Out Odd-Length Words and Convert to Uppercase
# words = ['apple', 'banana', 'cherry', 'date']
# # Expected Output: ['APPLE', 'CHERRY']
words = ['apple', 'banana', 'cherry', 'date']

uppercase_odd_length_words = list(filter(lambda x: len(x) % 2 != 0, words))
uppercase_odd_length_words = [x.upper() for x in uppercase_odd_length_words]
print(uppercase_odd_length_words)