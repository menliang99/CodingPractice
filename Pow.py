def pow(x, n):

	if n == 0:
		return 1.0
	elif n < 0:
		return 1 / pow(x, -n)
	elif n % 2:
		return pow(x*x, n/2)*x
	else:
		return pow(x*x, n/2)


def sqrt(x):
	
	if x == 0:
		return 0
	i = 1
	j = x / 2 + 1
	
	while i <= j:
		center = (i + j) / 2
		if center ** 2 == x:
			return center
		elif center ** 2 > x:
			j = center - 1
		else:
			i = center + 1
	return j








