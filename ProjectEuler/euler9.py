def pythagTriplet(maxNum):
    result = 0

    for x in range(1, maxNum):
        #print(str(x) + "...")
        for y in range(1, maxNum):
            for z in range(1, maxNum):
                if (x + y + z == maxNum and x * x + y * y == z * z):
                    return x * y * z
                    
if __name__ == '__main__':
    print(pythagTriplet(1000))
