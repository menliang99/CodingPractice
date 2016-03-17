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

	def mergesort(self, head):
		
		if head == None or head.next == None :
			return head
		slow = head
		fast = head.next
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		mid = slow.next
		slow.next = None
	
		self.mergesort(head)
		self.mergesort(mid)

		dummy = ListNode(0)
		newhead = dummy

		while mid and head:
			if (mid.val > head.val):
				dummy.next = head
				head = head.next
			else:
				dummy.next = mid
				mid = mid.next
			dummy = dummy.next

		if mid:
			dummy.next = mid
		else:
			dummy.next = head
		
		return newhead.next


code = Solution()
	
head = ListNode(0)
code.AddNode(head, 13)
code.AddNode(head, 12)
#head = head.next
code.PrintLL(head)

newhead = code.mergesort(head)
code.PrintLL(head)
code.PrintLL(newhead)
