print "Example of the args"

def Func(*args):
	for arg in args:
		print arg

Func(1, 2, 3, 4, "ham")
L = [1, 2, 3, 4, "ham"]
Func(L) # take the list as one parameter

Func(*L) # take in each element in the list

print "Example of the kwargs"

def Func2(**kwargs):
	for item in kwargs.items():
		print item

Func2(x = 456, y = 3)

print "omnipotent function input"

def Func3(*args, **kwargs):
	for arg in args:
		print arg
	for item in kwargs.items():
		print item
Func3(12, x = 3, y = 6)

