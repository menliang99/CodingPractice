#Figure out zip, map, lambda in python

def wordPattern(pattern, str):

	words = str.split()
	if len(pattern) != len(words):
		return False
	ptnDict, wordDict = {}, {}
	for ptn, word in zip(pattern, words):
		if ptn not in ptnDict:
			ptnDict[ptn] = word
		if word not in wordDict:
			wordDict[word] = ptn
		if wordDict[word] != ptn or ptnDict[ptn] != word:
			return False
	return True

def wordPatternII(pattern, str):
	s = pattern
	t = str.split()
	return map(s.find, s) == map(t.index, t)

def wordPatternIII(pattern, str):
	s = pattern
	t = str.split()
	return len(set(zip(s, t))) == len(set(s)) == len(set(t))

pattern = "abba"
str = "dog cat cat dog"

print wordPattern(pattern, str)
print wordPatternII(pattern, str)
print wordPatternIII(pattern, str)
