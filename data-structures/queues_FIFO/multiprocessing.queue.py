# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
from multiprocessing import Queue

q = Queue()
q.put('eat')
q.put('sleep')
q.put('repeat')

print(q)

print(q.get())
print(q.get())
print(q.get())