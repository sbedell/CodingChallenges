def isEven(n):
    return n % 2 == 0

def fibonacci(n):
    if n == 1 or n == 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibSequence(n):
    counter = 1
    totalSum = 0
    fibSeq = 0
    while(fibSeq < n):
        fibSeq = fibonacci(counter)
        if(isEven(fibSeq)):
            totalSum += fibSeq
        counter += 1
    return totalSum

if __name__ == '__main__':
    print(isEven(4))
    print(isEven(6))
    print(fibonacci(10))
    print(fibSequence(4000000))
    
