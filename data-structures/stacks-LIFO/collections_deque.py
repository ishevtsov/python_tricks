# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

s = deque()
s.append('eat')
s.append('sleep')
s.append('repeat')

print(s)

print(s.pop())
print(s.pop())
print(s.pop())