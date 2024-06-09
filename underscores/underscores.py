# Single Leading Underscore: "_var"
# --------------------------------
# meant a hint var is intended for internal use

class Test:
	def __init__(self):
		self.foo = 11
		self._bar = 23

t = Test()
print(t.foo)
print(t._bar)

# Single Trailing Underscore: "var_"
# --------------------------------
# is used by convention to avoid naming conflicts with Python keywords

# Double Leading Underscore: "__var"
# ---------------------------------
# causes the Python interpreter to rewrite the attribute name
# in order to avoid naming conflicts in subclasses.
# Name mangling - makes it harder to create collision when
# the class is extended later

class Test:
	def __init__(self):
		self.foo = 11
		self._bar = 23
		self.__baz = 42

t = Test()
print(dir(t))  # __baz mangled to _Test__baz

class ExtendedTest(Test):
	def __init__(self):
		super().__init__()
		self.foo = 'overridden'
		self._bar = 'overridden'
		self.__baz = 'overridden'

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
# print(t2.__baz) AttributeError: 'ExtendedTest' object has no attribute '__baz'.

print(dir(t2))  # __baz mangled to _ExtendedTest__baz

print(t2._ExtendedTest__baz)  # 'overridden'
print(t2._Test__baz)          # 42

# Double Leading and Trailing Underscore: "__var__"
# --------------------------------
# Not mangled and reserved for special use int he language.