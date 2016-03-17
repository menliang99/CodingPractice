def partition (A, p, q):
	i = p
	x = A[i]
	for j in range(p + 1, q + 1):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	A[p], A[i] = A[i], A[p]
	return i

def partitionII (A, p, q):
	print A
	print p
	print q
	start = p + 1
	end = q
	pivot = A[p]
	while True:

		while (A[end] >= pivot and start < end):   # sequence matters!!!
			end = end - 1
		while (A[start] <= pivot and start < end):
			start = start + 1

		if (start == end):
			break;
		A[start], A[end] = A[end], A[start]
	if A[p] < A[start]:
		return p
	A[p], A[start] = A[start], A[p]
	return start

def partitionIII (A, p, q):
	print A
	print p
	print q
	start = p
	end = q - 1
	pivot = A[q]
	while True:
		while (A[start] <= pivot and start < end):
			start = start + 1
		while (A[end] >= pivot and start < end):
			end = end - 1
		if (start == end):
			break;
		A[start], A[end] = A[end], A[start]
	if A[q] > A[start]:
		return q
	A[q], A[start] = A[start], A[q]
	return start


def quickSort(A, p, q):

	if p < q:
		r = partitionII(A, p, q)
		quickSort(A, p, r - 1)
		quickSort(A, r + 1, q)
	return A


array = [1, 12, 3, 5, 13, 9, 0, 0]
print "before sorting"
print array
p = 0
q = len(array) - 1
print q
quickSort(array, p, q)
print "after sorting"
print array
