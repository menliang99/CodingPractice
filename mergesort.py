
def mergesort(Arr):

	if len(Arr) <= 1:
		return

	mid = len(Arr) / 2
	lefthalf = Arr[:mid]
	righthalf = Arr[mid:]
	mergesort(lefthalf)
	mergesort(righthalf)
	
	i =  0
	j =  0
	k =  0

	while (i < len(lefthalf) and j < len(righthalf)):
		if lefthalf[i] < righthalf[j]:
			Arr[k] = lefthalf[i]
			i = i + 1
		else:
			Arr[k] = righthalf[j]
			j = j + 1
		k = k + 1
	
	while i < len(lefthalf):
		Arr[k] = lefthalf[i]
		i = i + 1
		k = k + 1

	while j < len(righthalf):
		Arr[k] = righthalf[j]
		j = j + 1
		k = k + 1

	return








def mergesortII(Arr):

	length = len(Arr)
	Brr = [None] * length #for step in range (1, length/2 + 2, step * 2):
	step = 1
	while step < length:  #bug Here!!

		for left in range(0, length - step, step * 2):
			firstend = left + step
			secondend = firstend + step
			if secondend > length:
				secondend = length	
			i = left
			j = firstend
			k = left

			while (i < firstend and j < secondend):
				if Arr[i] < Arr[j]:
					Brr[k] = Arr[i]
					i = i + 1
				else:
					Brr[k] = Arr[j]
					j = j + 1
				k = k + 1

			while (i < firstend):
				Brr[k] = Arr[i]
				k = k + 1
				i = i + 1
			while (j < secondend):
				Brr[k] = Arr[j]
				k = k + 1
				j = j + 1

			for k in range(left, secondend):
				Arr[k] = Brr[k]

		step = step * 2
	return




array = [9, 8, 3, 5, 18, 0, 7, 4, 10009, 2]
mergesortII(array)
print array



