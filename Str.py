
def strStr(haystack, needle):

	if haystack == None or needle == None:
		return -1

	if len(needle) == 0:
		return 0
	i = 0
	j = 0
	for i in range(0, len(haystack) - len(needle) + 1):
		for j in range(0, len(needle)):
			if haystack[i + j] != needle[j]:
				break
			if j == len(needle) - 1:
				return i
	return -1

haystack = ""
needle = ""

#print len(needle)
#print len(haystack)

print strStr(haystack, needle)
