# call function inside the class without instantiation them

class MyClass:
	@classmethod
	def printHam(self):
		print "HAM"
MyClass.printHam()
