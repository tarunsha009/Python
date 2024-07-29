from collections import defaultdict
from typing import List


def maximumSum(nums: List[int]) -> int:

    def get_digit_sum(num):
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //=10

        return digit_sum

    dict = defaultdict(list)
    for num in nums:
        digit_sum = get_digit_sum(num)
        dict[digit_sum].append(num)

    print(dict)

    ans = -1
    for key in dict:
        curr = dict[key]
        print(curr)
        if len(curr) > 1:
            curr.sort(reverse=True)
            print(curr)
            ans = max(ans, curr[0] + curr[1])
    # for key, val in dict.items():
    #     if len(val) > 1:
    #         total = sum(val)
    #         ans = max(ans, total)

    return ans



nums = [18,43,36,13,7]

print(maximumSum(nums))

# nums = [10,12,19,14]
# print(maximumSum(nums))
#
# nums = [368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]
# print(maximumSum(nums))