def GetLongestPal(s, l, r):
	while l >= 0 and r < len(s) and s[l] == s[r]:
		l -= 1
		r += 1
	return s[l+1 : r]

def LongestPal(s):
	pal = ''
	for i in range(len(s)):

		len1 = len(GetLongestPal(s, i, i))
		if len1 > len(pal):
			pal = GetLongestPal(s, i, i)

		len2 = len(GetLongestPal(s, i, i + 1)
		if len2 > len(pal):
			pal = GetLongestPal(s, i, i + 1)
	return pal


			
