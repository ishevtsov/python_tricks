# https://docs.python.org/3/library/queue.html#queue.PriorityQueue
from queue import PriorityQueue

q = PriorityQueue()

q.put((3, 'repeat'))
q.put((1, 'eat'))
q.put((2, 'sleep'))

while not q.empty():
	next_item = q.get()
	print(next_item)