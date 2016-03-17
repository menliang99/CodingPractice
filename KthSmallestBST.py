class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def SizeofTree(self, root):

		if root is None:
			return 0
		return SizeofTree(root.left) + SizeofTree(root.right) + 1

	def KthSmallest(self, root, k):
		if root is None:
			return 0
		leftsize = self.SizeofTree(root.left)
		if leftsize == k - 1:
			return root.val
		elif leftsize > k - 1:
			return self.KthSmallest(root.left, k)
		else:
			return self.KthSmallest(root.right, (k - 1 - leftsize))

	def KthSmallestII(self, root, k):
		Q = collections.deque(maxlen = k)
		while True:
			while root:
				Q.append(root)
				root = root.left
			root = Q.pop()
			if k == 1:
				return root.val
			k = k - 1
			root = root.right


