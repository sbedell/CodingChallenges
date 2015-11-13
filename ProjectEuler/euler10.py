import math
from euler3 import isPrime

def summationOfPrimes(n):
        totalSum = 0
        for i in range(2, n):
                if isPrime(i):
                        totalSum += int(i)
        return totalSum

if __name__ == '__main__':
        #print(summationOfPrimes(100))
        print(summationOfPrimes(2000001))
