class Node:
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None 

from sys import *

def MinDepth(root):

	if root is None:
		return 0
	if (root.left is None and root.right is None):
		return 1

	if root.left is not None:
		leftDepth = MinDepth(root.left)
	else:
		leftDepth = 10#sys.maxint

	if root.right is not None:
		rightDepth = MinDepth(root.right)
	else:
		rightDepth = 10#sys.maxint

	return 1 + min(leftDepth, rightDepth)

root = Node(1)
root.left = Node(0)
root.right = Node(9)
root.left.right = Node(8)

print MinDepth(root)
