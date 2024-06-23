from collections import deque

q = deque()
q.append('eat')
q.append('sleep')
q.append('repeat')
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
