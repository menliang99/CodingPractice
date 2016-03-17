from abc import ABCMeta, abstractmethod

class BaseClass(object):  # abstract class can not be instanted
	__metaclass__ = ABCMeta

	@abstractmethod  #decorator! way of altering functions or classes without having to inherit or subclass
	def printHam(self):
		pass

class InClass(BaseClass):
	def printHam(self):
		print "ham"

x = InClass()


