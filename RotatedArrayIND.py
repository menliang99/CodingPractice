def findPivot(arr):

	if arr == None:
		return -1
	if (arr[0] <= arr[-1]):
		return 0

	start = 0
	end = len(arr) - 1

	while (start <= end):
		mid = (start + end) / 2
		if (arr[mid] > arr[mid + 1]):
			return mid + 1
		elif (arr[start] <= arr[mid]):
			start = mid + 1
		else:
			end = mid - 1
	return 0

arr = [7, 8, 9, 1, 2, 3, 4]
print findPivot(arr)

def findElement(arr, target):

	pivot = findPivot(arr)
	
	if target > arr[0]:
		start = 0
		end = pivot - 1
	else:
		start = pivot 
		end = len(arr) - 1

	while (start <= end):
		mid = (start + end) / 2
		if (arr[mid] == target):
			return mid
		elif (arr[mid] > target):
			end = mid - 1
		else:
			start = mid + 1













