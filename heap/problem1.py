from heapq import *

heap = []

heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)


print(heap[0])
print(heappop(heap))
print(len(heap))
heappushpop(heap, 0)
heapreplace(heap, 3)
print(heap)

l = [10,34,12,45,20]
heapify(l)
print(l)
heappop(l)
print(l)
heappop(l)
print(l)
heapify

hea