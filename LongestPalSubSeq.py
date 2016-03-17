#https://www.youtube.com/watch?v=U4yPae3GEO0&index=7&list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI
#Number 7


def LPS(s):

	n = len(s)
	dp = [[1 for i in range(n)] for i in range(n)]

	for curlen in range(2, n + 1):
		for i in range(0, n - curlen + 1):
			j = i + curlen - 1
			if(s[i] == s[j]):
				dp[i][j] = dp[i + 1][j - 1] + 2
			else:
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
	return dp[0][n-1]

s = "LPASPAL"
print LPS(s)
