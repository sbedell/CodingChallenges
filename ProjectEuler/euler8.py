def buildBigNum(filename):
        bigNum = str()
        with open(filename, 'r') as f:
                for line in f:
                        bigNum += line.strip()
        return bigNum

def findGreatestProduct(num):
        pass

"""
dig1 = bigNum[0]
dig2 = bigNum[1]
dig3 = bigNum[2]
dig4 = bigNum[3]
dig5 = bigNum[4]
greatestProduct = int(dig1) * int(dig2) * int(dig3) * int(dig4) * int(dig5)

# Shift all down, get new greatest product
count = 5
for x in bigNum[5:]:
	#print x
	dig1 = dig2
	dig2 = dig3
	dig3 = dig4
	dig4 = dig5
	dig5 = bigNum[count]
	prod = int(dig1) * int(dig2) * int(dig3) * int(dig4) * int(dig5)
	if prod > greatestProduct:
		greatestProduct = prod
	count += 1
"""

if __name__ == '__main__':
        myBigNum = buildBigNum('euler8in')
        print(myBigNum)
        
        theGreatestProduct = 0
        myList = list()
        # Build initial sequence:
        for i in range(13):
                myList.insert(0, myBigNum[i])
        print(myList)

        tempGreatest = 1
        for x in myList:
                tempGreatest = tempGreatest * x
                if int(tempGreatest) > theGreatestProduct:
                        greatestProduct = int(tempGreatest)
