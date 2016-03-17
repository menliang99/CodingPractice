class TreeNode:

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BSTIterator:

	def __init__(self, root):
		self.stack = []
		self.pushLeft(root)

	def pushLeft(self, node):
		while node:
			self.stack.append(node)
			node = node.left

	def hasNext(self):
		return self.stack

	def next(self):
		top = self.stack.pop()
		self.pushLeft(top.right)
		return top.val

class BSTIteratorII:

	def __init__(self, root):
		self.tree = []
		self.inOrderTraverse(root)
		self.idx = -1
		self.size = len(self.tree)

	def hasNext(self):
		self.idx += 1
		return self.idx < self.size

	def next(self):
		return self.tree[self.idx]

	def inOrderTraverse(self, root):
		if root is None:
			return
		self.inOrderTraverse(root.left)
		self.tree.append(root.val)
		self.inOrderTraverse(root.right)









