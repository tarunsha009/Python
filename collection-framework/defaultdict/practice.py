from collections import defaultdict

counter = defaultdict(int)

for char in "Tarun":
    counter[char] +=1

print(counter)

