
def hIndexI(citations):
	
	for i, c in enumerate(sorted(citations, reverse = True)):
		if i >= c:
			return i

	return len(citations)

def hIndexII(citations):
	
	N = len(citations)
	for i, c in enumerate(sorted(citations)):
		if N - i <= c:
			return N - i
	return 0


def hIndexBS(citations):

	citations.sort()
	N = len(citations)
	low, high = 0, N - 1
	
	while low <= high:
		mid = (low + high) / 2
		if N - mid > citations[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return N - low


citations = [6, 6, 6, 1, 5]
print hIndexI(citations)
print hIndexBS(citations)

