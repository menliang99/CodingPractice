#dynamic programming: dp[x+c] = min(dp[x] + 1, dp[x+c])
#dp[x] means for the amount x, the minimum number of coins needed; c is the avaliable coin amount
#initialize dp[0] = 0
import collections

def coinChangeDP(coins, amount):

	dp = [0] + [-1] * amount

	for x in range(amount):
		print dp
		if dp[x] < 0:
			continue
		for c in coins:
			if x + c > amount:
				continue
			if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
				dp[x + c] = dp[x] + 1
	return dp[amount]

def coinChangeBFS(coins, amount):
	
	steps = collections.defaultdict(int)
	queue = collections.deque([0])
	steps[0] = 0

	while queue:
		front = queue.popleft()
		level = steps[front]
		if front == amount:
			return level
		for c in coins:
			if front + c > amount:
				continue
			if front + c not in steps:
				queue += front + c,
				steps[front + c] = level + 1
	return -1


coins = [1, 2, 5]
amount = 11

print coinChangeDP(coins, amount)
print coinChangeBFS(coins, amount)


