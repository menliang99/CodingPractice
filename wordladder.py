def LadderLength(start, end, dct):

	dct.add(end)
	print dct
	q = []
	q.append((start, 1))
	while q:
		print q
		curr = q.pop(0)
		currword = curr[0]
		currlen = curr[1]
		
		if currword == end:
			return currlen
		for i in range(len(start)):
			part1 = currword[:i]
			part2 = currword[i+1:]
			for j in 'abcdefghijklmnopqrstuvwxyz':
				if currword[i] != j:
					nextword = part1 + j + part2
					if nextword in dct:
						q.append((nextword, currlen + 1))
						dct.remove(nextword)
	return 0


start = "lot"
end = "dog"
test = ["lot", "lit", "dot", "dit", "lip", "dig"]
dct = set(test)

print dct
print LadderLength(start, end, dct)




