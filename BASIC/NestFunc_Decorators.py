def addOne(myFunc):
	def addOneInside():
		return myFunc() + 1
	return addOneInside


@addOne  #decorator!!
def oldFunc():
	return 3

#oldFunc = addOne(oldFunc)  can be replaced by decorator
print oldFunc()
