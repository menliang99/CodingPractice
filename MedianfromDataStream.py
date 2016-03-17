class Heap:

	def __init__(self, cmp):
		self.cmp = cmp
		self.heap = [None]

	def __swap__(self, x, y, a):
		a[x], a[y] = a[y], a[x]

	def size(self):
		return len(self.heap) - 1

	def top(self):
		return self.heap[1] if self.size() else None

	def append(self, num):
		self.heap.append(num)
		self.siftUp(self.size())

	def pop(self):
		top, last = self.heap[1], self.heap.pop()
		if self.size():
			self.heap[1] = last
			self.siftDown(1)
		return top

	def siftUp(self, idx):
		while idx > 1 and self.cmp(idx, idx / 2, self.heap):
			self.__swap__(idx / 2, idx, self.heap)
			idx /= 2
	
	def siftDown(self, idx):
		while idx * 2 <= self.size():
			nidx = idx * 2
			if nidx + 1 <= self.size() and self.cmp(nidx + 1, nidx, self.heap):
				nidx += 1
			if self.cmp(nidx, idx, self.heap):
				self.__swap__(nidx, idx, self.heap)
				idx = nidx
			else:
				break

class MedianFinder:
		
	def __init__(self):
		self.minHeap = Heap(cmp = lambda x, y, a : a[x] < a[y])
		self.maxHeap = Heap(cmp = lambda x, y, a : a[x] > a[y])

	def addNum(self, num):
		self.maxHeap.append(num)
		if self.minHeap.top() < self.maxHeap.top() or self.minHeap.size() + 1 < self.maxHeap.size():
			self.minHeap.append(self.maxHeap.pop())
		if self.maxHeap.size() < self.minHeap.size():
			self.maxHeap.append(self.minHeap.pop())

	def findMedian(self):
		if self.minHeap.size() < self.maxHeap.size():
			return self.maxHeap.top()
		else:
			return (self.minHeap.top() + self.maxHeap.top()) / 2.0

from heapq import *
class MedianFinderII:

	def __init__(self):
		self.minHeap = []
		self.maxHeap = []

	def addNum(self, num):
		heappush(self.maxHeap, -num)
		minTop = self.minHeap[0] if len(self.minHeap) else None
		maxTop = self.maxHeap[0] if len(self.maxHeap) else None

		if minTop < -maxTop or len(self.minHeap) + 1 < len(self.maxHeap):
			heappush(self.minHeap, -heappop(self.maxHeap))
		if len(self.maxHeap) < len(self.minHeap):
			heappush(self.maxHeap, -heappop(self.minHeap))

	def findMedian(self):
		if len(self.minHeap) < len(self.maxHeap):
			return -1.0 *  self.maxHeap[0]
		else:
			return (self.minHeap[0] - self.maxHeap[0]) / 2.0