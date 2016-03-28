# Garbage from getPrimeFactors iterative:

#if ((i * i > myNum) and (myNum > 1)):
        #    primeFactors.add(int(myNum))

    # start at 3, go up to num, step 2:
    #for i in range(3, myNum, 2):
    #    if (isPrime(i) and (myNum % i == 0)):
    #        primeFactors.append(i)

# ---- Garbage non working Recursive Attempt ----
def primeFactorsRecursive(num, i, factors):
    if (num <= i):
        #print("if")
        return set()
    elif num % i == 0:
        #print("elif")
        factors.add(i)
        return primeFactorsRecursive(num / i, i, factors)
    #print(i)
    i = i + 1
    return primeFactorsRecursive(num, i, factors)
