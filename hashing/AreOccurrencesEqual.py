from collections import defaultdict

s = "abacbc"
def areOccurrencesEqual(s: str) -> bool:
    count = defaultdict(int)
    for x in s:
        count[x] +=1

    frequency = count.values()
    print(frequency)
    return len(set(frequency)) == 1


print(areOccurrencesEqual(s))