def fn(s):
	order = []
	counts = {}
	
	for char in s:
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
			order.append(char)
			
	for char in order:
		if counts[char] == 1:
			return char
			
	return None


