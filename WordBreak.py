def wordBreak(s, dct):

	dp = [False for i in range(len(s) + 1)]
	dp[0] = True

	for i in range(1, len(s) + 1):
		for k in rnage(i):
			if dp[k] and s[k:i] in dct:
				dp[i] = True
	return dp[len(s)]


