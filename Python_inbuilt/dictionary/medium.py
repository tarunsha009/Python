# 1. Count Characters in a String
# Task: Write a dictionary comprehension that counts the occurrences of each character in a given string.
# text = "hello world"
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

text = "hello world"
char_count = {char: text.count(char) for char in set(text)}
print(char_count)

# 2. Reverse a Dictionary
# Task: Given a dictionary where the values are unique, create a new dictionary that reverses the keys and values.
# original_dict = {'a': 1, 'b': 2, 'c': 3}
# {1: 'a', 2: 'b', 3: 'c'}

original_dict = {'a': 1, 'b': 2, 'c': 3}
result = {v:k for k, v in original_dict.items()}
print(result)

# 3. Group Words by Length
# Task: Write a dictionary comprehension that groups a list of words by their lengths.
#
# Example Input:
# words = ["apple", "bat", "car", "banana", "kiwi"]
# {5: ['apple', 'banana'], 3: ['bat', 'car'], 4: ['kiwi']}


# 5. Merge Two Dictionaries
# Task: Given two dictionaries, merge them into one. If there are overlapping keys, sum their values.
#
# Example Input:
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 25, 'c': 35, 'd': 40}

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 25, 'c': 35, 'd': 40}

merged_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(merged_dict)



# Sum of Even and Odd Numbers:
#
# Task: Create a dictionary where the keys are numbers from 1 to 5 and the values are dictionaries with keys 'even' and 'odd' that sum the even and odd digits of the number.
# Input: range(1, 6)
# Expected Output:
# {
#     1: {'even': 0, 'odd': 1},
#     2: {'even': 2, 'odd': 0},
#     3: {'even': 0, 'odd': 3},
#     4: {'even': 4, 'odd': 0},
#     5: {'even': 0, 'odd': 5}
# }

output = {
    x: {
        'even': sum(int(digit) for digit in str(x) if int(digit) % 2 == 0),
        'odd': sum(int(digit) for digit in str(x) if int(digit) % 2 != 0)
    }
    for x in range(1, 6)
}

print(output)







