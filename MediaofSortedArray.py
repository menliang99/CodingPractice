def findMediaSortedArray(A, B):

	lenA = len(A)
	lenB = len(B)

	if (lenA + lenB) % 2 == 1:
		return getKth(A, B, (lenA + lenB)/2 + 1)
	else:
		return ( getKth(A, B, (lenA + lenB)/2) + getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

def getKth(A, B, k):
	lenA = len(A)
	lenB = len(B)
	if lenA > lenB: 
		return getKth(B, A, k)
	if lenA == 0:
		return B[k-1]
	if k == 1:
		return min(A[0], B[0])

	pa = min(k/2, lenA)
	pb = k - pa

	if A[pa-1] <= B[pb-1]:
		return getKth(A[pa:], B, pb)
	else:
		return getKth(A, B[pb:], pa)


		
