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

# Not 100% sure what these are for? old comments...
#num1 = 37107287533902102798797998220837590246510135740250
#num2 = 46376937677490009712648124896970078050417018260538