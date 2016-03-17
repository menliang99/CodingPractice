
def maxProduct(A):

	if len(A) == 0:
		return 0
	min_value = A[0]
	max_value = A[0]

	result = A[0]
	for i in range(1, len(A)):
		a = A[i] * max_value
		b = A[i] * min_value
		c = A[i]
		max_value = max(max(a, b), c)
		min_value = min(min(a, b), c)
		result = max(max_value, result)
	return result

A = [2, 3, -1, 4, 2]
print maxProduct(A)
