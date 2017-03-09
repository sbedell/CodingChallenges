#!/bin/python3
import sys

n = input().strip()

# your code goes here
def findNumReductions(n):
  MAX_VAL = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
  
  if (n == 0):
    return 1
  elif (n == 1):
    return 0
  # End Elif
  
  numOps = 0
  
  while (n > 1):
    #print("n = " + str(n))
    
    if (isEven(n)):
      n = n // 2
    elif (n == 3 or isMultipleOfFour(n - 1)):
      n = n - 1
    else:
      n = n + 1
    # end else
        
    numOps = numOps + 1
  #End While
  
  return numOps
# End FindNumReductions - I hate how python doesn't have ending curly braces lol

# ---------------------------------
def isEven(i):
  return i % 2 == 0

def isMultipleOfFour(i):
  return i % 4 == 0

# start "main"
if len(n) > 309:
    print("Error - input is too long")
elif int(n) < 0:
    print("Error - no negative numbers allowed")
else:
    print(findNumReductions(int(n)))
