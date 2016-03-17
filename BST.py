from collections import deque

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	
class Solution:


	def BuildTree(self, root, val):
		if val < root.val:
			if (root.left != None):
				self.BuildTree(root.left, val)
			else:
				root.left = TreeNode(val)
		else:
			if (root.right != None):
				self.BuildTree(root.right, val)
			else:
				root.right = TreeNode(val)

	def AddNode(self, root, val):
		newnode = TreeNode(val)
		if root == None:
			return newnode
		else:
			self.BuildTree(root, val)
		return root


	def PrintTree(self, root):
		if root == None:
			print "None"
		dummynode = None
		queue = deque([])
		queue.append(root)
		
		while queue:
			size = len(queue)
			print
			for i in range(0, size):
				node = queue.popleft()
				if node:
					print node.val, " ",
					if node.left:
						queue.append(node.left)
					else:
						queue.append(dummynode)
		
					if node.right:
						queue.append(node.right)
					else:
						queue.append(dummynode)
				else:
					print "None",
		print
		return

	def InorderPrint(self, root):

		if root == None:
			#print "None"
			return
		
		self.InorderPrint(root.left)
		print root.val, " ",
		self.InorderPrint(root.right)
		return

	def PreorderPrint(self, root):
		if root == None:
			return
		print root.val, " ",
		self.PreorderPrint(root.left)
		self.PreorderPrint(root.right)


	def PostorderPrint(self, root):
		if root == None:
			return
		self.PostorderPrint(root.left)
		self.PostorderPrint(root.right)
		print root.val, " ",


	def PreorderPrintII(self, root):
		
		if root == None:
			return
		
		stack = []
		stack.append(root)

		while stack:
			node = stack.pop()
			print node.val, " ",
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return

	def InorderPrintII(self, root):
		if root == None:
			return

		stack = []
		while stack or root:
			if root:
				stack.append(root)
				root = root.left
			else:
				node = stack.pop()
				print node.val, " ",
				root = node.right
		return


	def InorderPrintIII(self, root):

		stack = []
		self.pushleft(stack, root)
		while stack:
			node = stack.pop()
			print node.val,
			self.pushleft(stack, node.right)
		print

	def pushleft(self,stack,root):
		while root:
			stack.append(root)
			root = root.left
		return



code = Solution()
root = TreeNode(10)
code.AddNode(root, 1)
code.AddNode(root, 8)
code.AddNode(root, 0)
code.AddNode(root, 34)
code.AddNode(root, 11)
code.AddNode(root, 81)
code.AddNode(root, 19)
code.AddNode(root, 14)

print"LeveL Traversal:"
code.PrintTree(root)

print"Inorder Traversal:"
code.InorderPrintIII(root)
print
print"Preorder Traversal:"
code.PreorderPrint(root)
print
print"Postorder Traversal:"
code.PostorderPrint(root)














