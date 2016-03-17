
def rotateArray(nums, k):
	
	length = len(nums)
	k = k % length

	reverse(nums, 0, length - 1)
	reverse(nums, 0, k - 1)      # Intelligence Defence to figure out 
	reverse(nums, k, length - 1)

def reverse(nums, start, end):

	print nums
	
	while (start < end):
		nums[start], nums[end] = nums[end], nums[start]
		start = start + 1
		end = end - 1
	print nums



def rotateImage(matrix):

	n = len(matrix)

	for layer in range (0, n / 2):
		for pos in range (layer, n-layer-1):
			ref = matrix[pos][layer]
			print ref
			matrix[pos][layer] = matrix[layer][n - pos - 1]
			print matrix[pos][layer]
			matrix[layer][n - pos - 1] = matrix[n - pos - 1][n - layer - 1]
			print matrix[layer][n - pos - 1]
			matrix[n - pos - 1][n - layer - 1] = matrix[n - layer - 1][pos]
			print matrix[n - pos - 1][n - layer - 1]
			matrix[n - layer - 1][pos] = ref
			print


nums = [1, 2, 5, 6, 7]
k = 3

#rotateArray(nums, k)
#print nums

matrix = [[i for i in xrange(4)] for i in xrange(4)]
print matrix

rotateImage(matrix)
print matrix










