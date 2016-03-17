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

	def isSameTree(self, p, q):
		
		if (p == None and q == None):
			return True
		if (p == None or q == None or p.val != q.val):
			return False

		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

	
	def ReverseTree(self, p):
		if p == None:
			return
		self.reverseTree(p.left)
		self.reverseTree(p.right)

		p.left, p.right = p.right, p.left

	def isSymmetricTree(self, p):
		if p == None:
			return True

		return isSym_routine(root.left, root.right)

	def isSym_routine(self, leftnode, rightnode):

		if leftnode == None:
			return rightnode == None
	
		if rightnode == None:
			return leftnode == None

		if leftnode.val != rightnode.val:
			return False

		return isSym_routine(leftnode.left, rightnode.right) and isSym_routine(leftnode.right, rightnode.left)
	
	
	def minDepth(self, root):
		
		if root == None:
			return 0
		return self.minDepth_routine(root)

	def minDepth_routine(self, root):
		
		if root == None:
			return sys.maxint
		if root.left == None and root.right == None:
			return 1

		return min(self.minDepth_routine(root.left), self.minDepth_routine(root.right)) + 1

	def reverseTreeII(self, root):
		
		if root == None:
			return None
		if root.left == None and root.right == None:
			return root

		leftnode = self.reverseTreeII(root.left)
		rightnode = self.reverseTreeII(root.right)

		root.left = rightnode
		root.right = leftnode

		return root

	def TreePath(self, root):
		
		ret = []
		strlist = ""
		self.Path_routine(ret, root, strlist)
		return ret

	def Path_routine(self, ret, root, strlist):
		if root == None:
			return
		if root.left == None and root.right == None:
			strlist += str(root.val)
			print strlist
			return ret.append(strlist)
		strlist += str(root.val)
		strlist += "->"
		self.Path_routine(ret, root.left, strlist)
		#ret.pop()
		#ret.pop()
		self.Path_routine(ret, root.right, strlist)
		#ret.pop()
		#ret.pop()
		# it is not a loop, so you don't need to pop

	def invertTree(self, root):
		if root is None:
			return root
		queue = [root];
		while queue:
			front = queue.pop(0)
			if front.left:
				queue.append(front.left)
			if front.right:
				queue.append(front.right)
			front.left, front.right = front.right, front.left
		return root

	def invertTreeII(self, root):
		if root is None:
			return
		self.invertTreeII(root.left)
		self.invertTreeII(root.right)
		root.left, root.right = root.right, root.left
		return

	def isBalancedTree(self,root):
		if root is None:
			return True
		leftHeight = self.maxheight(root.left)
		rightHeight = self.maxheight(root.right)

		if abs(leftHeight - rightHeight) > 1 :
			return False
		return self.isBalancedTree(root.left) and self.isBalancedTree(root.right)

	def maxheight(self, root):
		if root is None:
			return 0
		return max(self.maxheight(root.left), self.maxheight(root.right)) + 1



code = Solution()
p = TreeNode(10)
code.AddNode(p, 1)
code.AddNode(p, 8)
code.AddNode(p, 0)
code.AddNode(p, 34)
code.AddNode(p, 11)
code.AddNode(p, 81)
code.AddNode(p, 19)
code.AddNode(p, 14)

print"LeveL Traversal:"
code.PrintTree(p)


q = code.invertTreeII(p)
code.PrintTree(p)

print code.isBalancedTree(p)















