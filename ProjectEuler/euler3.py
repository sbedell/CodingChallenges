import math

def isPrime(n):
        # SUPER SLOW ALGO
	for x in range(2, int(math.sqrt(n) + 1)):
		if n % x == 0:
			return False
	return True

def largestPrime(targetNum):
        largestFactor = 0
        for y in range(2, int(math.sqrt(targetNum))):
                if isPrime(y):
                        if targetNum % y == 0:
                                largest = y

        return largest

if __name__ == '__main__':
        print(isPrime(29))
        # print(isPrime(345))
        # print(isPrime(8951))
        # print(isPrime(6857))
        print(largestPrime(600851475143))
