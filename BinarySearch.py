def BinarySearch(Array, num):	
	start = 0
	end = len(Array)
	while start + 1 < end:
		mid = start + (end - start) / 2
		if Array[mid] == num:
			return mid
		elif Array[mid] > num:
			end = mid
		else:
			start = mid	
	if A[start] == num:
		return start
	elif A[end] == num:
		return end
	else:
		return -1

def RotatedSearch(Array, num):
	start = 0
	end = len(Array)
	while start + 1 < end:
		mid = start + (end - start) / 2
		if (Array[mid] == num):
			return mid
		if (Array[start] < A[mid]):
			if (num < Array[mid] and num > Array[start]):
				end = mid
			else:
				start = mid
		else:
			if (num > Array[mid] and num < Array[end]):
				start = mid
			else:
				end = mid
	if A[start] == num :
		return start
	if A[end] == num :
		return end
	return -1		

A = [0, 1, 2, 3, 14, 15, 15, 26, 27, 38, 49]
print BinarySearch(A, 15) 
