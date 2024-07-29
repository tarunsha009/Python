from collections import defaultdict
from typing import List

def minimumCardPickup(cards: List[int]) -> int:
    count = {}
    start = 0
    ans = float("inf")
    for end in range(len(cards)):
        value = cards[end]
        count[value] = count.get(value , 0) + 1
        while count[value] > 1:
            count[cards[start]] -=1
            ans = min(ans, end - start + 1)
            start +=1

        # ans = min(ans, end - start)

    return ans if ans < float("inf") else -1





cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))
cards = [1,0,5,3]
print(minimumCardPickup(cards))

cards = [95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]

print(minimumCardPickup(cards))