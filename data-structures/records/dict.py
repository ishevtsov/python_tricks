car1 = {
	'color': 'red',
	'mileage': 3812.4,
	'automatic': True,
}
car2 = {
	'color': 'blue',
	'mileage': 40231,
	'automatic': False,
}

print(car1)

print(car2['mileage'])

car2['mileage'] = 12
car2['windshield'] = 'broken'
print(car2)
