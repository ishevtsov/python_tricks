import functools

def uppercase(func):
	@functools.wraps(func)
	def wrapper():
		return func().upper()
	return wrapper

@uppercase
def greet():
	'''Return a friendly greeting'''
	return 'Hello!'

print(greet.__name__)
print(greet.__doc__)