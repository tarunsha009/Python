from typing import List


def largestAltitude(nums: List[int]) -> int:
    prefix = [0] * (len(nums) + 1)
    highest = prefix[0]
    for i in range(len(nums)):
        prefix[i + 1] = nums[i] + prefix[i]
        highest = max(highest, prefix[i + 1])

    return highest

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))