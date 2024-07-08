from typing import List


# An array of boolean values is divided into two sections: The left section consists of all false, and the right
# section consists of all true. Find the First True in a Sorted Boolean Array of the right section, i.e.,
# the index of the first true element. If there is no true element, return -1.
#
# Input: arr = [false, false, true, true, true]
#
# Output: 2
#
# Explanation: The first true's index is 2.

def find_boundry(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans



print(find_boundry([False, False, True, True, True]))
print(find_boundry([False,False, False,False]))
# all true
print(find_boundry([True, True, True, True, True]))



# Given an array of integers sorted in increasing order and a target, find the index of the first element in the
# array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.
#
# Input:
#
# arr = [1, 3, 3, 5, 8, 8, 10]
# target = 2
# Output: 1
#
# Explanation: The first element larger than 2 is 3, which has index 1.
#
# Input:
#
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: 3
#
# Explanation: The first element larger than 6 is 7, which has index 3.
def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) -1
    ans = -1
    while left<=right:
        mid = (left + right) // 2
        if arr[mid]>= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

print(first_not_smaller([1, 3, 3, 5, 8, 8, 10], 2))


# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its
# index. Return -1 if the target is not in the array.
#
# Input:
#
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1
#
# Explanation: The first occurrence of 3 is at index 1.
#
# Input:
#
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1
#
# Explanation: 6 does not exist in the array.


def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) -1
    ans = -1
    while left<=right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

return ans

print(find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))
print(find_first_occurrence([2, 3, 5, 7, 11, 13, 17, 19], 6))