import math

def isPrime(n):
        # Pretty Horrible alorgithm for huge numbers:
	for x in range(2, int(math.sqrt(n) + 1)):
		if n % x == 0:
			return False
	return True

def summationOfPrimes(n):
        totalSum = 0
        for i in range(2, n):
                if isPrime(i):
                        totalSum += int(i)
        return totalSum

if __name__ == '__main__':
        #print(summationOfPrimes(100))
        print(summationOfPrimes(2000001))
