# https://docs.python.org/3/library/queue.html#queue.LifoQueue
from queue import LifoQueue

s = LifoQueue()

s.put('eat')
s.put('sleep')
s.put('repeat')

print(s)

print(s.get())
print(s.get())
print(s.get())