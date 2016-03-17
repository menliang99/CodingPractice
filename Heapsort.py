#keypoint to remember: root, root*2+1,  root*2+2 are in the same tree. 
#Create max-heap using bottom up method
#SiftDown: Repeatedly delete the largest remaining item from the root 

def HeapSort(A):

	def heapify(A):
		start = (len(A) - 2) / 2
		while start >= 0:
			print start, A[start]
			siftDown(A, start, len(A) - 1)
			start = start - 1
			print A

	def siftDown(A, start, end):
		root = start
		while root * 2 + 1 <= end:
			child = root * 2 + 1
			if child + 1 <= end and A[child] < A[child + 1]:
				child = child + 1
			if child <= end and A[root] < A[child]:
				A[root], A[child] = A[child], A[root]
				root = child
			else:
				return

	print "before heapify", A
	heapify(A)
	print "Max heap after heapify", A
	end = len(A) - 1
	while end > 0:
		A[end], A[0] = A[0], A[end]
		end = end - 1
		siftDown(A, 0, end)
	print "After heapsorting", A

A=[4, 6, 9, 2, 0, 19, 7, 1]

HeapSort(A)


