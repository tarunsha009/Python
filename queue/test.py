from collections import deque

q = deque()
print(q)
q1 = deque((1,2,3,4,5))

print(q1)

q2 = deque([1,2,3,4,5])
print(q2)

q2.pop()
print(q2)
q2.popleft()
print(q2)
q2.count(2)
print(q2)
q2.appendleft(11)
print(q2)
q2.extend([21,22,33,44])
print(q2)
q2.extendleft([99,22,33,44])
print(q2)
print(q2.pop())
