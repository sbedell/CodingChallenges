import time

def getPrimeFactors(myNum):
    primeFactors = set()
    i = 2

    while myNum > 1:
        while myNum % i == 0:
            primeFactors.add(i)
            myNum = int(myNum / i)    
        i = i + 1
    return sorted(primeFactors)

# Recursive Attempt
def primeFactorsRecursive(num, i):
    if num < i:
        return set()
    if num % i == 0:
        x = set()
        x.add(i)
        return sorted(x.union(primeFactorsRecursive(num / i, 2)))
    return sorted(primeFactorsRecursive(num, i + 1))

# ----- Testing -----:
print("Non Recursive Testing:")

start = time.time()
print(getPrimeFactors(200))
print(getPrimeFactors(2500))
print(getPrimeFactors(10000000000))
print(getPrimeFactors(9999999999))
print(getPrimeFactors(99999999999))
print(getPrimeFactors(9898989898))
print(getPrimeFactors(4294967295))

print("\nRuntime =", time.time() - start, "ms")
print("---------------------------------------")
print("Recursive Testing:\n")

start = time.time()
print(primeFactorsRecursive(200, 2))
print(primeFactorsRecursive(2500, 2))
print(primeFactorsRecursive(56565, 2))
print(primeFactorsRecursive(565656, 2))
print(primeFactorsRecursive(5656565, 2))
print(primeFactorsRecursive(56565656, 2))

# Starts stack overflowing from here on out:
# print(sorted(primeFactorsRecursive(565656565, 2)))
# print(primeFactorsRecursive(9999999999, 2))
# print(primeFactorsRecursive(4294967295, 2))

print("\nRuntime =", time.time() - start, "ms")
