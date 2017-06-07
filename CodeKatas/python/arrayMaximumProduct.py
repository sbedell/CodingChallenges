#!/bin/python3

'''
Maximum product of an array subset

[2,-3,1,0,-5] answer would be 30
[2,0,2,2,0] would be 8
[-2,-3,4,-5] would be 60
'''
                
def countNegatives(myList):
    negativeNums = 0
    
    for n in myList:
        if int(n) < 0:
            negativeNums = negativeNums + 1
    return negativeNums

def getBiggestNeg(myList):
    maxNeg = -1000
    for x in myList:
        if int(x) < 0 and int(x) > maxNeg:
            maxNeg = int(x)
    return maxNeg

def isAllZeroes(myList):
    allZeroes = True
    for n in myList:
        if int(n) != 0:
            allZeroes = False
    return allZeroes

def findMaxProduct(myList):
    # Check for zeroes:
    if isAllZeroes(xs):
        return str(0)
    
    # If there are an odd number of negatives, we'll need to remove one of em
    if(countNegatives(xs) % 2 != 0):
        maxNeg = getBiggestNeg(xs)
        xs.remove(str(maxNeg)) # need to force it to int

    # Actually do the calculations:
    product = 1
    for x in xs:
        y = int(x)
        if y != 0 and abs(y) <= 1000:
            product = product * y
    return product
            
#---------------------------------------------------
xs = input().strip().split(",")

if len(xs) > 50:
    print("Error - only 50 length allowed")
else:
    print(findMaxProduct(xs))