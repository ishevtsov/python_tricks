# Lambdas are single-expression Functions
add = lambda x, y: x + y
print(add(5, 3))

# Lambda is inline function that we can defins and call immediately
print((lambda x, y: x + y)(5, 3))

# You can use lambdas any time you're expected to supply a function
# object.
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(tuples)

sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

# Lambdas work as closures
def make_adder(n):
	return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))