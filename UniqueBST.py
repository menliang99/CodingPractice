# Catalan number

def numTrees(n):
	dp = [1, 1, 2]
	if n <= 2:
		return dp[n]
	else:
		dp += [0 for i in range(n - 2)] # numbers in the array will increase here!
		print dp
		for i in range(3, n + 1):
			for j in range(1, i + 1):
				dp[i] += dp[j-1] * dp[i-j]
		print dp
		return dp[n]

def generateTrees(n):
	return dfs(1, n)




print numTrees(10)



