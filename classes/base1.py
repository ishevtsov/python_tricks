class Base:
	def foo(self):
		raise NotImplementedError()

	def bar(self):
		raise NotImplementedError()

class Concrete(Base):
	def foo(self):
		return 'foo() called'

c = Concrete()
c.foo()
c.bar()