# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from  typing import List
def longestOnes(nums: List[int], k: int) -> int:
    start = 0;
    ans = 0
    zero_count = 0
    # current_size = 0
    for end in range(len(nums)):
        value = nums[end]
        if value == 0 and zero_count == k:
            while zero_count == k:
                if nums[start] == 0:
                    zero_count -=1
                start += 1

            # current_size = 1
            # zero_count = 1
            # continue
        if value == 0 and zero_count < k:
            zero_count +=1

        current_size = end - start +1
        ans = max(current_size, ans)

    return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(longestOnes(nums, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums, k))
