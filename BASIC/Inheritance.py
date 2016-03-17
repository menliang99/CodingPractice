class Character(object):
	def __init__(self, name):
		self.health = 100
		self.name = name
	def printName(self):
		print self.name

class Blacksmith(Character):
	def __init__(self, name, forgeName):
		super(Blacksmith, self).__init__(name) # call the init function from the base class
		self.forge = Forge(forgeName)

class Forge:
	def __init__(self, forgeName):
		self.name = forgeName

bs = Blacksmith("Bob", "rick\'s forge")
bs.printName()
print bs.forge.name
