def collatzChainLength(n):
    chainLen = 1
    temp = n
    while(temp != 1):
        if (temp % 2 == 0):
            temp = temp / 2
        else:
            temp = (3 * temp) + 1
        chainLen += 1
    return chainLen

def longestChain(maxNum):
    maxLen = 0
    num = 0
    for i in range(maxNum):
        cl = collatzChainLength(i)
        if (cl > maxLen):
            maxLen = cl
            num = i
    return num, maxLen

if __name__ == '__main__':
    # ans = 837799
    # print(collatzChainLength(13))
    #print(longestChain(1000000))
    print(collatzChainLength(837799))
    print(collatzChainLength(899999))
    
