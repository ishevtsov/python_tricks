class Dog:
	num_legs = 4

	def __init__(self, name):
		self.name = name

jack = Dog('Jack')
jill = Dog('Jill')

print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)

print(Dog.num_legs)