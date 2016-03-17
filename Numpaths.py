def numpaths(grid):
	row = len(grid)
	col = len(grid[0])
	return numpathsrec(grid, row-1, col-1)

def numpathsrec(grid, row, col):
	if m < 0 or n < 0 or grid[m][n] == 0:
		return 0
	if m == 0 and n == 0:
		return 1
	return 1 + numpathsrec(grid, m - 1, n) + numpathsrec(grid, m, n - 1) + numpathsrec(grid, m - 1, n - 1)



