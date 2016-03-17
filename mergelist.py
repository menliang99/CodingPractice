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

	def MergeList(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		dummy = ListNode(0)
		newhead = dummy
		while l1 and l2:
			if (l1.val < l2.val):
				dummy.next = l1
				l1 = l1.next
			else:
				dummy.next = l2
				l2 = l2.next
			dummy = dummy.next
		if l1 == None:
			dummy.next = l2
		else:
			dummy.next = l1

		return newhead.next

code = Solution()
	
l1 = ListNode(0)
code.AddNode(l1, 71)
code.AddNode(l1, 18)

l2 = ListNode(3)
code.AddNode(l2, 19)
code.AddNode(l2, 28)
code.AddNode(l2, 23)

print "Before Merge"
code.PrintLL(l1)
code.PrintLL(l2)

l3 = code.MergeList(l1, l2)


print "After Merge"
code.PrintLL(l1)
code.PrintLL(l2)
code.PrintLL(l3)


