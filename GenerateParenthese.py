
def helper(l, r, item, res):
	if r < l:
		return
	if l == 0 and r == 0:
		res.append(item)
	if l > 0:
		helper(l - 1, r, item + '(', res)
	if r > 0:
		helper(l, r - 1, item + ')', res)

def GenerateParenthesis(n):
	if n == 0:
		return []
	res = []
	helper(n, n, '', res)
	return res

