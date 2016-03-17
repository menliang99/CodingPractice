class Node:
	__init__(self, key):
		self.val = key
		self.next = None

def isPal(head):
	if head is None:
		return True

	fast = slow = head
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

	p, last = slow.next, None
	while p:
		tmp = p.next
		p.next = last
		last = p
		p = tmp
	
	p1, p2 = last, head
	while p1 and p1.val == p2.val:
		p1, p2 = p1.next, p2.next

	p, last = last, None
	while p:
		tmp = p.next
		p.next = last
		last = p
		p =  tmp
	
	slow.next = last
	return p1 is None











	
