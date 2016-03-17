#make sure the leftmost index in the queue is the largest in the current array

def maxSlidingWindow(nums, k):

	dq = []
	ans = []
	for i in range(0, len(nums)):
		print dq
		while dq and nums[dq[-1]] <= nums[i]:
			dq.pop()
		dq.append(i)
		if dq[0] == i - k:
			dq.pop(0)
		if i >= k - 1:
			ans.append(nums[dq[0]])
	return ans

nums = [1, 2, 3, 5, 7, 19, 20, 30]

nums.reverse()
k = 3

print nums

print maxSlidingWindow(nums, k)
