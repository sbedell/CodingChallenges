import time

def getPrimeFactors(myNum):
    primeFactors = set()
    i = 2

    while myNum > 1:
        while myNum % i == 0:
            primeFactors.add(i)
            myNum = int(myNum / i)
        i += 1
    return sorted(primeFactors)

# Recursive Attempt
def getPrimeFactorsRecursive(num, i):
    if num < i:
        return set()
    if num % i == 0:
        x = set()
        x.add(i)
        return sorted(x.union(getPrimeFactorsRecursive(num / i, 2)))
    return sorted(getPrimeFactorsRecursive(num, i + 1))

# ----- Testing -----:
if __name__ == '__main__':
    print("Non Recursive Testing:")

    start = time.time()
    print(getPrimeFactors(200)) #2, 5
    print(getPrimeFactors(2500))
    print(getPrimeFactors(10000000000))
    print(getPrimeFactors(9999999999)) # 3, 11, 41, 271, 9091
    print(getPrimeFactors(99999999999)) # 3, 21649, 513239
    print(getPrimeFactors(9898989898)) # 2, 7, 41, 271, 9091
    print(getPrimeFactors(4294967295)) # 3, 5, 17, 257, 65537

    print("\nRuntime =", time.time() - start, "ms")
    print("---------------------------------------")
    print("Recursive Testing:\n")

    start = time.time()
    print(getPrimeFactorsRecursive(200, 2)) #2, 5
    print(getPrimeFactorsRecursive(2500, 2)) #2, 5
    print(getPrimeFactorsRecursive(56565, 2)) # 3, 5, 419
    print(getPrimeFactorsRecursive(565656, 2)) # 2, 3, 7, 13, 37
    print(getPrimeFactorsRecursive(5656565, 2)) # 5, 41, 673
    print(getPrimeFactorsRecursive(56565656, 2)) # 2, 7, 73, 101, 137

    #print(getPrimeFactorsRecursive(99999999999, 2)) Stack overflow

    # Starts stack overflowing from here on out:
    # print(sorted(getPrimeFactorsRecursive(565656565, 2)))
    # print(getPrimeFactorsRecursive(9999999999, 2))
    # print(getPrimeFactorsRecursive(4294967295, 2))

    print("\nRuntime =", time.time() - start, "ms")
