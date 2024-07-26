from typing import List


arr = [1,2,3]
def countElements(arr: List[int]) -> int:
    new_set = set(arr)
    count = 0
    for item in arr:
        if item+1 in new_set:
            count +=1

    return count



print(countElements(arr))
print(countElements([1,1,3,3,5,5,7,7]))
