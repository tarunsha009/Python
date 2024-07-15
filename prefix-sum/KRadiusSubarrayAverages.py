from typing import List


def getAverages(nums: List[int], k: int) -> List[int]:
    if k == 0:
        return nums

    window_size = 2 * k + 1

    result = [-1] * len(nums)
    if window_size > len(nums):
        return result
    prfix_sum = [0] * (len(nums) +1)
    # n = len(nums)
    # prefix = [0] * (n + 1)
    # for i in range(n):
    #     prefix[i + 1] = prefix[i] + nums[i]
    # print(prefix)
    for i in range(len(nums)):
        prfix_sum[i+1] = prfix_sum[i] + nums[i]

    print(prfix_sum)

    for i in range(k , len(nums) - k):
        leftBound, rightBound = i - k, i + k
        subArraySum = prfix_sum[rightBound + 1] - prfix_sum[leftBound]
        average = subArraySum // window_size
        result[i] = average
        # result[i] = (prfix_sum[i + k] - prfix_sum[i - k]) // window_size
    return result

nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(getAverages(nums, k))
print(getAverages([100000], 0))
print(getAverages([8], 100000))