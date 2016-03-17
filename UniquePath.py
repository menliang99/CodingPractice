
def uniquepathII(m, n):

# From the top-left cell to bottom-right cell, there are totoally
# m+n-2 moves. Among these moves, m-1 is moving downwards, and 
# n-1 is moving to right. So the number of possible unique paths = C(m+n-2, m-1) = C(m+n-2, n-1)


	if m <= 0 or n <= 0:
		return 0

	result = 1
	total = m + n - 2
	chosen = min(m, n) - 1
	
	for i in range(total, total - chosen, -1):
		result *= i
	for i in range(chosen):
		result //= (i+1)

	return result

def uniquepath(m, n):

	if m <= 0 or n <= 0:
		return 0
	
	grid = [[0 for x in range(n)] for x in range(m)]
	grid[0][0] = 0

	for i in range (1, m):
		grid[i][0] = 1
	for i in range(1, n):
		grid[0][i] = 1

	for i in range (1, m):
		for j in range(1, n):
			grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

	return grid[m - 1][n - 1]

def climbStairs(n):
	
	fun = [1 for x in range(n + 1)]
	
	for i in range(2, n + 1):
		fun[i] = fun[i - 1] + fun[i - 2]

	return fun[n]


m = 0
n = 4

print uniquepath(m, n)
print uniquepathII(m, n)

print climbStairs(n)
