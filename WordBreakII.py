
class Solution:

	def wordBreak(self, s, dct):
		Solution.res = []
		self.dfs(s, dct, '')
		return Solution.res

	def dfs(self, s, dct, stringlist):
		if self.check(s, dict):
			if len(s) == 0:
				Solution.res.append(stringlist[1:])
			for i in range(1, len(s) + 1):
				if s[:i] in dct:
					self.dfs(s[i:], dct, stringlist + ' ' + s[:i])
	def check(self, s, dict):
		dp = [False for i in range(len(s) + 1)]
		dp[0] = True
		for i in range(1, len(s) + 1):
			for k in range(0, i):
				if dp[k] and s[k:i] in dict:
					dp[i] = True
		return dp[len(s)]




