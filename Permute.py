
def CombSum(candidates, target):

	candidates.sort()
	result = []
	Comb_routineII(candidates, target, [], result)
	return result

def Comb_routine(candidates, target, prelist, result):

	#print candidates

	if target < 0:
		return

	if target == 0:
		result.append(list(prelist))

	for i in range (0, len(candidates)):
		prelist.append(candidates[i])
		Comb_routine(candidates[i:], target - candidates[i], prelist, result)
		prelist.pop()


def Comb_routineII(candidates, target, prelist, result):

	#print candidates

	if target < 0:
		return

	if target == 0:
		result.append(list(prelist))

	for i in range (0, len(candidates)):
		if (i > 0 and candidates[i] == candidates[i - 1]):  #remove duplicate from the top level
			continue
		prelist.append(candidates[i])
		Comb_routineII(candidates[i+1:], target - candidates[i], prelist, result) # remove duplicate from the lower level
		prelist.pop()


candidates = [10, 1, 2, 7, 6, 1, 5, 1]
result = CombSum(candidates, 8)

print result
