import math
from euler3 import isPrime

def findNthPrime(n):
        count = 1
        num = 2
        while (count <= n):
                if isPrime(num):
                        count += 1
                num += 1
        return num

if __name__ == '__main__':
        print(findNthPrime(100))