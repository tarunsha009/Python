def subsequences(index, result, list, length):
    if index == length:
        print(result)
        return
    # First take that index element and then call the function
    result.append(list[index])
    subsequences(index + 1, result, list, length)
    result.pop()
    # Then don't take that index element and then call the function
    subsequences(index + 1, result, list, length)

def subsequences_with_sum(index, result, list, length, sum, target_sum):
    if index == length:
        if sum == target_sum:
            print(result)
        return
    # First take that index element and then call the function
    result.append(list[index])
    sum = sum + list[index]
    subsequences_with_sum(index + 1, result, list, length, sum, target_sum)
    result.pop()
    sum = sum - list[index]
    # Then don't take that index element and then call the function
    subsequences_with_sum(index + 1, result, list, length, sum, target_sum)

list = [1, 2, 1]
subsequences_with_sum(0, [], list, len(list), 0, 2)
# subsequences(0, [], list, len(list))