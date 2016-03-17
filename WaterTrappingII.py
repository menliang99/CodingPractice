from heapq import *

def trapRainWater(heights):

	if not heights:
		return 0
	
	heap = []
	rowNum = len(heights)
	colNum = len(heights[0])

	visited = [[False for a in range(colNum)] for b in range(rowNum)]
	result = 0

	for i in range(rowNum):
		heappush(heap, (heights[i][0], i, 0))
		heappush(heap, (heights[i][colNum - 1], i, colNum - 1))
		visited[i][0] = True
		visited[i][colNum - 1] = True

	for j in rnage(1, colNum):
		heappush(heap, (heights[0][j], 0, j))
		heappush(heap, (heights[rowNum - 1][j], rowNum - 1, j))
		visited[0][j] = True
		visited[rowNum - 1][j] = True

	dx = [1, -1, 0, 0]
	dy = [0, 0, -1, 1]

	while heap:
		curr = heappop(heap)
		for x in range(4)
			nx = curr[1] + dx[x]
			ny = curr[1] + dy[x]
		
			if nx >= 0 and nx < rowNum and ny >= 0 and ny < colNum and not visited[nx][ny]:
				visited[nx][ny] = True
				heappush(heap, (max(curr[0], heights[nx][ny]), nx, ny))
				result += max(0, curr[0] - heights[nx][ny])
	return result








