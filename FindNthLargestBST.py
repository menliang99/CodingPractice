def FindNthLargest(root, n, count):  #count need to be passed by reference

	if root is None:
		return None

	Nth_Largest = FindNthLargest(root.right, n, count)

	if (Nth_Largest is None):
		count[0] += 1
		if (count[0] == n):
			Nth_Largest = root

	if (Nth_Largest is None):
		Nth_Largest = FindNthLargest(root.left, n, count)

	return Nth_Largest


