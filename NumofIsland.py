class DFSolution:

	def numIslands(self, grid):
		
		row = len(grid)
		if row == 0:
			return 0

		col = len(grid[0])
		marker = [[True for x in range(col)] for x in range(row)]
		ret = 0
		for i in range(0, row):
			for j in range(0, col):
				if grid[i][j] == '1' and marker[i][j] == True:
					self.search(i, j, grid, marker)
					ret = ret + 1
		return ret

	def search(self, i, j, grid, marker):
		marker[i][j] = False
		if i + 1 < len(grid) and grid[i+1][j] == '1' and marker[i+1][j] == True:
			self.search(i+1, j, grid, marker)
		if j + 1 < len(grid[0]) and grid[i][j+1] == '1' and marker[i][j+1] == True:
			self.search(i, j+1, grid, marker)
		if i - 1 >= 0 and grid[i-1][j] == '1' and marker[i-1][j] == True:
			self.search(i-1, j, grid, marker)
		if j - 1 >= 0 and grid[i][j-1] == '1' and marker[i][j-1] == True:
			self.search(i, j-1, grid, marker)











class BFSolution:

	def numIslands(self, grid):
		row = len(grid)
		if row == 0:
			return 0
		col = len(grid[0])

		marker = [[True for x in range(col)] for x in range(row)]
		ret = 0 
		q = []

		for i in range(0, row):
			for j in range(0, col):
				if grid[i][j] == '1' and marker[i][j] == True:
					q.append([i, j])
					marker[i][j] = False
					while q:
						ii = q[0][0]
						jj = q[0][1]
						q.pop(0)

						if ii + 1 < len(grid) and grid[ii+1][jj] == '1' and marker[ii+1][jj] == True:
							q.append([ii + 1, jj])
							marker[ii+1][jj] = False
						if jj + 1 < len(grid[0]) and grid[ii][jj+1] == '1' and marker[ii][jj+1] == True:
							q.append([ii, jj+1])
							marker[ii][jj+1] == False										
						if ii - 1 >= 0 and grid[ii-1][jj] == '1' and marker[ii-1][jj] == True:
							q.append([ii - 1, jj])
							marker[ii+1][jj] = False
						if jj - 1 >= 0 and grid[ii][jj-1] == '1' and marker[ii][jj-1] == True:
							q.append([ii, jj-1])
							marker[ii][jj-1] == False
					ret = ret + 1

		return ret

		
















				
