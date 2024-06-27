def bounded_repeater(value, max_repeats):
	for i in range(max_repeats):
		yield value


for x in bounded_repeater('Hi', 4):
	print(x)