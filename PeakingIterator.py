# Decorator Pattern is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. 

class PeekingIterator(object):
	def __init__(self, iterator):
		self.iter = iterator
		self.peekFlag = False
		self.nextElement = None
	
	def peek(self):
		if not self.peekFlag:
			self.nextElement = self.iter.next()
			self.peekFlag = True
		return self.nextElement

	def next(self):
		if not self.peekFlag:
			return self.iter.next()
		nextElement = self.nextElement
		self.peekFlag = False
		self.nextElement = None
		return nextElement

	def hasNext(self):
		return self.peekFlag or self.iter.hasNext()




