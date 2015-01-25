import math

def isPrime(n):
	for x in range(2, int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True

targetNum = 600851475143
largestFactor = 0
for y in xrange(2, int(math.sqrt(targetNum))):
	if isPrime(y):
		if targetNum % y == 0:
			largest = y

print largest

# print isPrime(29)
# print isPrime(345)
# print isPrime(8951)
# print isPrime(6857)
