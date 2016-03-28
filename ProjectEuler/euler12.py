import sys, math

def triangleNum(num):
	tri = 0
	for i in range(1, num + 1):
		tri += int(i)
		#print(i)
	return tri

def numDivisors(num):
	divs = [1, num] # list?
	for i in range(2, num/2 + 1):
		if num % i == 0:
			if divs.count(i) == 0:
				divs.append(i)
	return divs

# ###############################333333333

# int(round(math.sqrt(num), 0))

# print triangleNum(7)
# print numDivisors(10)
#print len(numDivisors(28))

greatestDivLen = 0
for i in range(5000, 10000):
	if i % 80 == 0: print(i)
	length = len(numDivisors(triangleNum(i)))
	if length > greatestDivLen:
		greatestDivLen = length

print(greatestDivLen)
