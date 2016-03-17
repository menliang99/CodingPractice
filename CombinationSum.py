class Solution:

	ret = []
	def DFS(self, candidate, target, start, valuelist):
		length = len(candidates)
		if target == 0:
			return Solution.ret.append(valuelist)
		for i in range(start, length):
			if target < candidates[i]:
				return
			if i > 0 and candidates[i] == candidates[i - 1]:  # remove duplicate
				continue
			self.DFS(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])	  # i + 1: each element only use once.

	def combinationSum(self, candidates, target):
		candidates.sort()
		#Solution.ret = []
		self.DFS(candidates, target, 0, [])
		return Solution.ret

candidates = [1, 2, 2, 3, 2, 1]
target = 6

code = Solution()
print code.combinationSum(candidates, target)
