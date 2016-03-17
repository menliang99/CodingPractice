#Not count sort,  using partition ALG in quick sort. It is a one-pass ALG.

def sortColors(A):

	if A == []: return
	p0 = 0
	p2 = len(A) - 1
	i = 0

	while i <= p2:
		if A[i] == 2:
			A[i], A[p2] = A[p2], A[i]
			p2 = p2 - 1
		else A[i] == 0:
			A[i], A[p0] = A[p0], A[i]
			p0 = p0 + 1
			i = i + 1
		else:
			i = i + 1

