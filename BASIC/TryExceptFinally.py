try:
	x = 5 + 'ham'
except ZeroDivisionError:
	print 'will not see this'
finally:
	print 'the final word'


