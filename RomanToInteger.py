def RomanToInt(s):

	numerals = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

	ret = 0
	s = s[::-1]
	last = None
	for x in s:
		if last and numerals[x] < last:
			ret -= 2*numerals[x]        #reverse input and minors twice the value if it is less
		ret += numerals[x]
		last = numerals[x]
	return ret


def IntToRoman(num):
	values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	ret = ''
	for i in range(0, len(values)):
		while num >= values[i]:
			num -= values[i]
			ret += numerals[i]
	return ret


























