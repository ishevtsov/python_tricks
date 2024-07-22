def dispatch_if(operator, x, y):
	if operator == 'add':
		return x + y
	elif operator == 'sub':
		return x - y
	elif operator == 'mul':
		return x * y
	elif operator == 'div':
		return x / y


result = dispatch_if('mul', 2, 8)
print(result)

result = dispatch_if('unknown', 2, 8)
print(result)
print()

def dispatch_dict(operator, x, y):
	return {
		'add': lambda: x + y,
		'sub': lambda: x - y,
		'mul': lambda: x * y,
		'div': lambda: x / y,
	}.get(operator, lambda: None)()


result = dispatch_dict('mul', 2, 8)
print(result)

result = dispatch_dict('unknown', 2, 8)
print(result)