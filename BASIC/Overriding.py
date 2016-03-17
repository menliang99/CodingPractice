class BaseClass(object):
	def test(self):
		print "hom"

class InClass(BaseClass):
	def test(self):  # function overriding
		print "hammer time"

#print BaseClass.__subclasses__()  # find the inheritance class
i = InClass()
i.test

