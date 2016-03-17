# the comma in python merge things

def addOperators(num, target):

	def isLeadingZeros(num):
		return num.startswith('00') or int(num) and num.startswith('0')
	def solve(num, target, mulExpr = '', mulVal = 1):
		ans = []
		if isLeadingZeros(num):
			pass
		elif int(num) * mulVal == target:
			ans += num + mulExpr,
		for x in range(len(num) - 1):
			lnum, rnum = num[:x+1], num[x+1:]
			if isLeadingZeros(rnum):
				continue
			right, rightVal = rnum + mulExpr, int(rnum) * mulVal
			for left in solve(lnum, target - rightVal):
				ans += left + '+' + right,
			for left in solve(lnum, target + rightVal):
				ans += left + '-' + right,
			for left in solve(lnum, target, '*' + right, rightVal):
				ans += left,
		return ans
	if not num:
		return []
	return solve(num, target)


num = "123"
target = 6

print addOperators(num, target)
