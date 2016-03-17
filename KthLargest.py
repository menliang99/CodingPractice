def partition(arr, left, right, pivotIndex):

	arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
	pivot = arr[right]

	swapIndex = left

	for i in range(left, right):
		if arr[i] < pivot:
			arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
			swapIndex += 1

	arr[right], arr[swapIndex] = arr[swapIndex], arr[right]
	return swapIndex

def KthLargest(arr, left, right, k):

	if not 1 <= k <= len(arr):
		return
	if left == right:
		return arr[left]

	while True:

		pivotIndex = random.randint(left, right)
		pivotIndex = partition(arr, left, right, pivotIndex)

		rank = pivotIndex - left + 1
		if rank == k:
			return arr[pivotIndex]
		elif k < rank:
			return KthLargest(arr, left, pivotIndex - 1, k)
		else:
			return KthLargest(arr, pivotIndex + 1, right, k - rank)


			
