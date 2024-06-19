class Car:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def __str__(self):
		return '__str__ for Car'

	def __repr__(self):
		return '__repr__ for Car'

my_car = Car('red', 37456)
print(my_car)