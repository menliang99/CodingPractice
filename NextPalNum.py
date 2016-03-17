def reverse(num):
	ret = 0:
	while num > 0:
		ret = ret * 10 + num % 10
		num = num / 10
	return ret

def NextPal(num):
	if num == reverse(num):
		return num
	while True:
		num = num + 1
		if num == reverse(num):
			return num


