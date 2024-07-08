from collections import deque, Counter

# The function rotate_left_till_zero() takes an integer array containing one 0 and rotates the array counterclockwise
# so that the 0 ends up at the front of the array.

def rotate_left_till_zero(nums):
    queue = deque(nums)
    while queue[0] != 0:
        queue.append(queue.popleft())
    return queue


print(rotate_left_till_zero([1,2,0,4,5]))

word = "tarun sharma"
counter = Counter(word)
print(counter)
print(counter['t'])
print(counter.most_common(1))
print(len(counter))