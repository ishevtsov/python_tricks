class Car:
	def __init__(self, color, mileage, automatic):
		self.color = color
		self.mileage = mileage
		self.automatic = automatic

car1 = Car('red', 3812.4, True)
car2 = Car('blue', 40567.3, False)

print(car2.mileage)

car2.mileage = 12
car2.windshield = 'btoken'

print(car1)