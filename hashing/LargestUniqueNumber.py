from collections import Counter
from typing import List
def largestUniqueNumber(nums: List[int]) -> int:
    count = Counter(nums)
    print(count)
    largest = -1
    for key, val in count.items():
        if val == 1:
            largest = max(largest, key)

    return largest




nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(largestUniqueNumber(nums))
print(largestUniqueNumber([9,9,8,8]))