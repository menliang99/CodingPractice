class Node:
	__init__(self, x):
		self.val = x
		self.right, self.left = None, None


def ValidBST(root, min, max):
	if root == None:
		return True
	if root.val <= min or root.val >= max:
		return False
	return ValidBST(root.left, min, root.val) and ValidBST(root.right, root.val, max)

def isValidBST(root):
	return ValidBST(root, -2147483648, 2147483647)



