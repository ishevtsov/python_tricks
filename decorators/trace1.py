import functools

def trace(f):
	@functools.wraps(f)
	def decorated_function(*args, **kwargs):
		print(f, args, kwargs)
		result = f(*args, **kwargs)
		print(result)
	return decorated_function

@trace
def greet(greeting, name):
	return f'{greeting}, {name}!'

greet('Hello', 'Bob')