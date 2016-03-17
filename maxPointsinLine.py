class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class Solution:

	def maxpoints(self, points):

		length = len(points)
		if length < 3:
			return length
		res = -1

		for i in range(length):
			slope = {'inf': 0}  ##hashtable = {slope, NumberofPointsExceptItself}

			samePointNum = 1
			for j in range(length):
				if i == j:
					continue
				elif points[i].x == points[j].x and points[i].y != points[j].y:
					slope['inf'] += 1
				elif points[i].x != points[j].x:
					k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
					if k not in slope:
						slope[k] = 1
					else:
						slope[k] += 1
				else:
					samePointNum += 1
				print slope 
				print samePointNum
			res = max(res, max(slope.values()) + samePointNum)
		return res

code = Solution()
p1 = Point(0, 0)
p2 = Point(0, 1)
p3 = Point(0, 1)
p4 = Point(0, 1)
p5 = Point(8, 12)


pit = [p1, p2, p3, p4, p5]

print code.maxpoints(pit)







