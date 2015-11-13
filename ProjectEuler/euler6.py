import math

def sumSquareDifference(n):
        # Find squareSum
        squareSum = 0
        for x in range(1, n):
                squareSum += int(math.pow(int(x), 2))

        # Find digit sum
        digSum = 0
        for y in range(1, n):
                digSum += int(y)

        digSumSquared = int(math.pow(int(digSum), 2))
        return digSumSquared - squareSum

if __name__ == '__main__':
        #print "diff = " + str(int(digSumSquared - squareSum))
        print("diff = " + str(sumSquareDifference(101)))
