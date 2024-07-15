from typing import List


def reverseOnlyLetters(s: str) -> str:
    arr = []
    for item in s:
        arr.append(item)
    start, end = 0 , len(arr)-1
    while start < end:
        if arr[start].isalpha() and arr[end].isalpha():
            arr[start] , arr[end] = arr[end], arr[start]
            # arr[start] = v1
            # arr[end] = v2
            start +=1
            end -=1
        if not arr[start].isalpha():
            start += 1
        if not arr[end].isalpha():
            end -=1

    return "".join(arr)

s = "ab-cd"
print(reverseOnlyLetters(s))

print(reverseOnlyLetters("a-bC-dEf-ghIj"))