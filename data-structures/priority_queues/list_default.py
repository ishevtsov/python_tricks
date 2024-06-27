q = []

q.append((3, 'repeat'))
q.append((1, 'eat'))
q.append((2, 'sleep'))
print(q)

q.sort(reverse=True)
print(q)

while q:
	next_item = q.pop()
	print(next_item)