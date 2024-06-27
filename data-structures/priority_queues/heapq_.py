# https://docs.python.org/3/library/heapq.html
import heapq

q = []

heapq.heappush(q, (3, 'repeat'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (2, 'sleep'))

print(q)

while q:
	next_item = heapq.heappop(q)
	print(next_item)