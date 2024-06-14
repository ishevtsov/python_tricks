# Toy function
def yell(text):
	return text.upper()

print(yell('hello'))

# Functions are objects
bark = yell
print(bark('hello'))

# Functions and their names are two diff concerns
del yell
print(bark('hey'))

# Functions can be passed to other functions
def greet(func):
	greeting = func('Hi, I am a Python program')
	print(greeting)

greet(bark)


def whisper(text):
	return text.lower()

greet(whisper)

# Functions can be nested
def speak(text):
	def whisper(t):
		return t.lower() + '...'
	return whisper(text)

print(speak('Hello, World!'))

# You can return the inner function to the caller of the parent function
def get_speak_func(volume):
	def whisper(text):
		return text.lower() + '...'
	def yell(text):
		return text.upper() + '!'
	if volume > 0.5:
		return yell
	else:
		return whisper

print(get_speak_func(0.3))
print(get_speak_func(0.7))

speak_func = get_speak_func(0.7)
print(speak_func('Hello'))

# Functions can capture local state. Closures
def get_speak_func(text, volume):
	def whisper():
		return text.lower() + '...'
	def yell():
		return text.upper() + '!'
	if volume > 0.5:
		return yell
	else:
		return whisper

print(get_speak_func('Hello, World', 0.7)())

# Objects can behave like Functions
class Adder:
	def __init__(self, n):
		self.n = n

	def __call__(self, x):
		return self.n + x
plus_3 = Adder(3)
print(plus_3(4))