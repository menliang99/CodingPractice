BaseClass = type("BaseClass", (object,), {})  #use type is another way to create class!!
C1 = type("C1", (BaseClass,), {"x":1})
C2 = type("C2", (BaseClass,), {"x":30})

def MyFactory(myBool):
	return C1() if myBool else C2()

m = MyFactory(True)
v = MyFactory(False)

print m.x, v.x


##clear method of Factory###

#see FactoryATClass2.py


