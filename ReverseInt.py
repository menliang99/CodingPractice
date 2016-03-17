def reverse(x):
	ans = 0

	sign = 1 if x > 0 else -1

	x = abs(x)

	while x > 0:
		ans = ans * 10 + x % 10
		x = x / 10

	return sign * ans

