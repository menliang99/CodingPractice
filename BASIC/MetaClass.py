class Singleton(type):
	_instances =  {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
			cls.x = 5
		return cls._instances[cls]


class MyClass(object):
	__metaclass__ = Singleton
	def __init__(self, *args, **kwargs):
		super(Myclass, self).__init__(*args, **kwargs)

m = MyClass()
v = MyClass()

print m.x
m.x = 9
print v.x


