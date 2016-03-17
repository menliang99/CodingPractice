import threading, random, time

try:
	import Queue
except:
	import queue as Queue

class Producer:
	def __init__(self):
		self.food = ["ham", "soup", "salad"]
		self.nextTime = 0
	def run(self):
		global q
		while (time.clock() < 10):
			if (self.nextTime < time.clock()):
				f = self.food[random.randrange(len(self.food))]
				q.put(f)
				print ("Adding  " + f)
				print q
				self.nextTime += random.random()  # generate a ramdom floating number from 0 to 1
class Consumer:
	def __init__(self):
		self.nextTime = 0
	def run(self):
		global q
		while (time.clock() < 10):
			if (self.nextTime < time.clock() and not q.empty()):
				f = q.get()
				print("Removing  " + f)
				print q
				self.nextTime += random.random() * 2


if __name__ == '__main__':
	q = Queue.Queue(10)
	p = Producer()
	c = Consumer()
	pt = threading.Thread(target = p.run, args = ())
	ct = threading.Thread(target = c.run, args = ())
	pt.start()
	ct.start()



