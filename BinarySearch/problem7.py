# A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30,
# 40, 50, 10, 20]. Find the index of the minimum element in this array.
#
# Input: [30, 40, 50, 10, 20]
#
# Output: 3
#
# Explanation: The smallest element is 10, and its index is 3.
#
# Input: [3, 5, 7, 11, 13, 17, 19, 2]
#
# Output: 7
#
# Explanation: The smallest element is 2, and its index is 7.

from typing import List

def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0,  len(arr) -1
    res = -1
    while left <=right:
        mid = (left + right) //2
        if arr[mid] <= arr[-1]:
            right = mid -1
        else:
            left = mid +1
    return left


print(find_min_rotated([30, 40, 50, 10, 20]))
print(find_min_rotated([3, 5, 7, 11, 13, 17, 19, 2]))
