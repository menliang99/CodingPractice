def ThreeSum(nums):

	nums.sort()
	res = []

	for i in range((len(nums) - 2):
		if i == 0 or nums[i] > nums[i - 1]:
			left = i + 1
			right = len(nums) - 1
			while left < right:
				if nums[left] + nums[right] + nums[i] == 0:
					res.append([nums[i], nums[left], nums[right]])
					left = left + 1
					right = right - 1
					while left < right and nums[left] == nums[left - 1]:
						left = left + 1
					while left < right and nums[right] == nums[right + 1]:
						right = right - 1
				elif nums[left] + nums[right] + nums[i] < 0:
					left = left + 1
					if nums[left] == nums[left - 1]:
						break
				else:
					while left < right:
						right = right - 1
						if nums[right] < nums[right + 1]:
							break
	return res
