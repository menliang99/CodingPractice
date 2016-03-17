from abc import ABCMeta, abstractmethod

class Enemy(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def attackPlayer(self, player):
		pass

class EnvironmentAsset(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def __init__(self):
		self.mobile = False

class Trap(Enemy, EnvironmentAsset):
	def __init__(self):
		super(Trap, self).__init__()

	def attackPlayer(self, player):
		return player.health - 10

x = Trap()


