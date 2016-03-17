BaseClass = type("BaseClass", (object,), {})

@classmethod
def Check1(self, myStr):
	return myStr == "ham"

@classmethod
def Check2(self, myStr):
	return myStr =="sandwich"

C1 = type("C1", (BaseClass,), {"x":1, "Check":Check1})
C2 = type("C2", (BaseClass,), {"x":30, "Check":Check2})

def MyFactory(myStr):
	for cls in BaseClass.__subclasses__():
		if cls.Check(myStr):
			return cls()

m = MyFactory("ham")
v = MyFactory("sandwich")
print m.x, v.x



###creat the same thing without type #####

class AltBaseClass(object):
	pass

class AltC1(AltBaseClass):
	def __init__(self, *args, **kwargs):
		self.x = 1
	@classmethod
	def Check(self, myStr, *args, **kwargs):
		return myStr == "ham"

class AltC2(AltBaseClass):
	def __init__(self, *args, **kwargs):
		self.x = 30
	@classmethod
	def Check(self, myStr, *args, **kwargs):
		return myStr == "sandwich"

def AltMyFactory(myStr):
	for cls in AltBaseClass.__subclasses__():
		if cls.Check(myStr):  #call the class method without instance, use keyword @classmethod
			return cls()

print (AltMyFactory("ham").x)
print (AltMyFactory("sandwich").x)


