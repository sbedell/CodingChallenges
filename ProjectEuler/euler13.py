def largeSum(inputFile):
    count = 0
    totalSum = 0
    for num in file_in:
        #print str(count) + " " + str(num)
        totalSum = totalSum + int(num)
        count = count + 1
    return totalSum

if __name__ == '__main__':
    file_in = open('euler13infile', 'r')
    largeSum = largeSum(file_in)
    file_in.close()
    print(largeSum)
    print(str(largeSum)[0:10])
