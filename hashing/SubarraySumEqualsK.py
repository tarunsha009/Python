from collections import defaultdict
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, 2, 1, 2, 1]
k = 3

print(subarraySum(nums, k))


def numberOfSubarrays(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, 1, 2, 1, 1]
k = 3

numberOfSubarrays(nums, k)