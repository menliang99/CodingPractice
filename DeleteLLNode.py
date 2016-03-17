
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self, head):
		self.head = head

	def insert(self, data):
		new_node = ListNode(data)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count = count + 1
			current = current.get_next()
		return count

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("data not in the list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
	def printll(self):
		current = self.head
		while current:
			


ll = LinkedList(None)
ll.insert(9)
ll.insert(10)
ll.insert(11)

num = ll.size()
print num




