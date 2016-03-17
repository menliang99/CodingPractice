
def invtree(root):

	if root is None:
		return root

	dq=[root]

	while dq:
		front = dq.pop(0)
		if front.left:
			dq.append(front.left)
		if front.right:
			dq.append(front.right)
		front.left, front.right = front.right, front.left
	return root

