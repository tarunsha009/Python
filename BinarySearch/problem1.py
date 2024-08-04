from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low , high = 0, len(nums)-1
    if target > nums[high]:
        return high + 1
    elif target < nums[low]:
        return low
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid -1

    return low




nums = [1,3,5,6]
target = 4
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))
