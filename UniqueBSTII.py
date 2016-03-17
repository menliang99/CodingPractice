class TreeNode:
	def __init__(self, key):
		self.val = key
		self.right = None
		self.left = None

def dfs(start, end):
	if start > end: 
		return None
	res = []
	for rootval in range(start, end + 1):
		LeftTree = dfs(start, rootval - 1)
		RightTree = dfs(rootval + 1, end)
		for i in LeftTree:
			for j in RightTree:
				root = TreeNode(rootval)
				root.left = i
				root.right = j
				res.append(root)
	return res

def generateTrees(n):
	return dfs(1, n)
