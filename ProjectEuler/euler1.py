def sumOfMultiples(x, y):
        totalSum = 0
        for i in range(1, 1000):
                if ((i % x == 0) or (i % y == 0)):
                        totalSum = totalSum + i
        return totalSum

# -------------------------------------
if __name__ == '__main__':
        print(sumOfMultiples(3, 5))
