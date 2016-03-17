class Node:
	__init__(self, key):
		self.val = key
		self.left = None
		self.right = None



def buildTree(ind, postd):
	if len(postd) == 0:
		return None
	root = Node(postd[-1])
	idx = ind.index(postd[-1])

	rlen = len(ind[idx+1:])
	llen = len(ind) - rlen - 1

	if rlen > 0 :
		root.right = buildTree(ind[idx+1:], postd[-(rlen+1):-1])
	if llen > 0 :
		root.left = buildTree(ind[0:idx], postd[0:llen])
	return root

def buildTree2(ind, pred):
	if not ind: 
		return None
	root = Node(pred[0])
	idx = ind.index(pred[0])
	root.left = buildTree2(pred[1 : 1 + idx], ind[ : idx])
	root.right = buildTree2(pred[idx + 1 : ], ind[idx + 1: ])
	return root



