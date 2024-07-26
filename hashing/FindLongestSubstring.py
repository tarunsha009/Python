# find_longest_substring
# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
from collections import defaultdict
def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for end in range(len(s)):
        counts[s[end]] += 1
        while len(counts) > k:
            counts[s[left]] -=1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left +=1

        ans = max(ans, end - left + 1)

    return ans


print(find_longest_substring("eceba", 2))