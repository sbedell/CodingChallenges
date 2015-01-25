import sys, math

def isPrime(n):
	# range starts with 2 and goes to sqrt of n
	for x in range(2, int(math.sqrt(n)+1)):
		if n % x == 0:
			return False
	return True

count = 1
num = 2
while (count <= 10001):
	if isPrime(num):
		count = count + 1
		print num
	num = num + 1
