def RemoveDup(A):

	if len(A) == 0:
		return 0
	j = 0
	for i in range(len(A)):
		if A[i] != A[j]:
			A[i], A[j + 1] = A[j + 1], A[i]
			j = j + 1
	return j + 1

def RemoveElem(A, elem):
	j = len(A) - 1
	for i in range(len(A) - 1, -1, -1):
		if A[i] == elem:
			A[i], A[j] = A[j], A[i]
			j = j - 1
	return j + 1
