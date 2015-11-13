def selfPowers(n):
        totalSum = 0
        for i in range(1, n):
                totalSum += int(i**i)
        return totalSum

if __name__ == '__main__':
        totalSum = selfPowers(1001)
        # print(totalSum)
        print(str(totalSum)[-10:])
