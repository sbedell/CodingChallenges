import math

def isPrime(n):
    if (n % 2 == 0):
        return (n == 2)

    # start at 3, go up to sqrt(n) + 1
    # step of 2 to only cycle thru odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            return False
    return True
