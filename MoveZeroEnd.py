def MoveZeroEnd(A):

	if A is None:
		return
	for i in range (0, len(A) - 1):
		if (A[i] == 0):
			for j in range(i + 1, len(A)):
				if A[j] != 0:
					A[i], A[j] = A[j], A[i]
					break
		if (A[i] == 0):
			return

def MoveZeroEnd2(A):

	nZero = 0
	for i in range (0, len(A)):
		if A[i] == 0:
			nZero += 1
			continue
		if nZero > 0:
			A[i - nZero] = A[i]
			A[i] = 0


A=[0, 0, 1, 3, 0, 8, 9, 12, 0, 4, 7, 0]

MoveZeroEnd2(A)

print A
