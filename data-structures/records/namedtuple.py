# https://docs.python.org/3/library/typing.html#typing.NamedTuple
from typing import NamedTuple

class Car(NamedTuple):
	color: str
	mileage: float
	automatic: bool

car1 = Car('red', 3816.4, True)

print(car1)

# car1.mileage = 12
# car1.windshield = 'broken'