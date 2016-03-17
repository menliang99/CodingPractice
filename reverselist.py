class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def AddNode(self, head, x):
		current = head
		newnode = ListNode(x)
		if head == None:
			return newnode
		while head.next:
			head = head.next
		head.next = newnode
		return current

	def PrintLL(self, head):

		while head:
			print head.val,"-->",
			head = head.next
		print "None"

	def ReverseListI(self, head):
		if head == None :
			return head

		newhead = None
		while head:
			tmp = head.next
			head.next = newhead
			newhead = head
			head = tmp
		return newhead

	def ReverseListII(self, head):
		stack = []
		while head:
			stack.append(head)
			head = head.next

		dummy = ListNode(0)
		newhead = dummy

		while stack:
			dummy.next = stack.pop()
			dummy = dummy.next
		dummy.next = None

		return newhead.next
		
	def ReverseListIII(self, head):
		if head == None or head.next == None:
			return head
		SecHead = head.next
		#head.next = None
		PreHead = self.ReverseListIII(SecHead)
		SecHead.next = head   #Line Beyond Intelligence
		head.next = None		
		return PreHead


code = Solution()
	
head = ListNode(0)
code.AddNode(head, 1)
code.AddNode(head, 8)
code.AddNode(head, 89)
code.AddNode(head, 34)

head1 = ListNode(0)
#head1 = head1.next
#head = head.next
code.PrintLL(head)

newhead = code.ReverseListIII(head)
code.PrintLL(newhead)
