from collections import defaultdict
from typing import List

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

def intersection(nums: List[List[int]]) -> List[int]:
    count = defaultdict(int)
    for arr in nums:
        for n in arr:
            count[n] +=1
    result = []
    for key in count:
        if count[key] == len(nums):
            result.append(key)

    return sorted(result)


print(intersection(nums))