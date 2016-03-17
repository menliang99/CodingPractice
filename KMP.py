
def ShortestPal(s):

	rev_s = s[::-1]
	l = s + '#' + rev_s

	p = [0] * len(l)
	for i in range(1, len(l)):
		j = p [i - 1]
		while j > 0 and l[i] != l[j]:
			print "loop j", j, p
			j = p[j - 1]
		p[i] = j + (l[i] == l[j])
		print "loop i", i, p
	print p, p[-1]
	return rev_s[: len(s) - p[-1]] + s

s = "abvgfdba"
print ShortestPal(s)
