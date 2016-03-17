class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

def PostOrderTraveral(root):

	if root is None:
		return []
	stack = [root]
	ans = []

	while stack:
		top = stack.pop()
		ans.append(top.val)
		if top.left:
			stack.append(top.left)
		if top.right:
			stack.append(top.right)

	return ans[::-1]  # reverse the order

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print PostOrderTraveral(root)
