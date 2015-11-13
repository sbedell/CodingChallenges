import math

def factorialDigitSum(n):
        totalSum = 0
        for char in str(math.factorial(n)):
                totalSum += int(char)
        return totalSum

if __name__ == '__main__':
    print(factorialDigitSum(100))
