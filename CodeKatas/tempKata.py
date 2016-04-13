# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered closest to zero
# (for instance, if the temperatures are -5 and 5, then display 5).
# Your program must read input data and write the result on the standard output.

with open("codeKataTemps.txt", "r") as f:
    #Input Line 1: N, the number of temperatures to analyze, 0 ≤ N < 1,000,000
    n = int(f.readline())
    assert n >= 0 and n < 1000000 # 0 ≤ N < 1,000,000
        
    #Input Line 2: The N space delimited temperatures
    # expressed as integers ranging from -273 to 5526
    numbers = f.readline().strip().split(" ")

    # Display 0 (zero) if no temperatures are provided.
    # Otherwise, display the temperature closest to 0.
    if n == 0:
        print(0)
    else:
        #assert len(numbers) == n, "number of elements must be equal to the N on line 1"
        lowestTemp = -273
        for i in numbers:
            x = int(i)
            #assert x > -273 and x < 5526, "integer temps must range from -273 to 5526"
            if x < -273 or x > 5526:
                continue #skip the number

            if abs(x) < abs(lowestTemp):
                lowestTemp = x
            elif abs(x) == abs(lowestTemp):
                if x > 0 and lowestTemp < 0:
                    lowestTemp = x

        print(lowestTemp)
