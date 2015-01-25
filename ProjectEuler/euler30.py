import math

totalSum = 0
for i in range(2, 200000):
	tot = 0	
	for dig in str(i):
		tot += int(math.pow(int(dig), 5))
	if i == tot:
		print "FOUND ONE: " + str(tot)
		totalSum += int(tot)

print totalSum

# got it correct yayay
