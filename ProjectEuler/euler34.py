import math

def getFactorialDigs(n):
	totalSum = 0
	for i in str(n):
		totalSum += int(math.factorial(int(i)))
	return totalSum

n = 3
while n > 2:
	#print getFactorialDigs(n)
	if n == getFactorialDigs(n):
		print "HOLY SHIT " + str(n)
	n += 1
