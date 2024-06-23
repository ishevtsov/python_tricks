from queue import Queue

q = Queue()
q.put('eat')
q.put('sleep')
q.put('repeat')

print(q)

print(q.get())
print(q.get())
print(q.get())

# q.get_nowait()
# q.get()