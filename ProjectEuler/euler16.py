import math

def powerDigitSum(n):
        expo = 2**1000
        summ = 0
        
        for x in str(expo):
                summ += int(x)

        return summ
