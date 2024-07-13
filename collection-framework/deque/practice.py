# Question 1: Implement a Queue using Deque
# Problem Statement:
# Implement a queue using deque from the collections module. Your queue should have the following operations:
#
# enqueue(x): Add an element x to the end of the queue.
# dequeue(): Remove and return the front element of the queue.
# peek(): Return the front element of the queue without removing it.
# is_empty(): Return True if the queue is empty, False otherwise.


from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        top_element = self.queue.popleft()
        self.queue.appendleft(top_element)
        return top_element

    def is_empty(self):
        return len(self.queue) == 0


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.is_empty())  # Output: False
print(queue.dequeue())  # Output: 3
print(queue.is_empty())  # Output: True


# Question 2: Maximum of All Subarrays of Size K
# Problem Statement:
# Given an array of integers and a number k, find the maximum value in each subarray of length k.
# # Example usage:
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# Expected Output: [3, 3, 5, 5, 6, 7]

def max_subarray(nums, k):
    result = []
    dq = deque()

    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

            # Remove elements smaller than the current element from the deque
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

            # Add the current element's index to the deque
        dq.append(i)

        # Append the maximum element in the current sliding window to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_subarray(nums, k)
# Expected Output: [3, 3, 5, 5, 6, 7]


def subarray(nums, k):
    result = []
    dq = deque()
    max_so_far = 0
    for i in range(k):
        max_so_far = max(max_so_far, nums[i])
        dq.append(nums[i])

    result.append(max_so_far)
    for i in range(k , len(nums)):

        value = nums[i]

        while len(dq) >= k:
            dq.popleft()

        max_so_far = max(max_so_far,  value)

        dq.append(value)
        result.append(max_so_far)

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
output = subarray(nums, k)
print("result: ", output)
# Expected Output: [3, 3, 5, 5, 6, 7]