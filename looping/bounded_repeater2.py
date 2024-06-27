def bounded_repeater(value, max_repeats):
	count = 0
	while True:
		if count >= max_repeats:
			return
		count += 1
		yield value

for x in bounded_repeater('Hi', 4):
	print(x)