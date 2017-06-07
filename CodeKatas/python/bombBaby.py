#!/bin/python3

def isSolvable(m, f):
    return (m > 0 and f > 0 and (m != f))

def answer(m, f):
    numberOfSteps = 0
    
    if m == f:
        return "impossible"
    elif f == 1 and m > f:
        numberOfSteps = m - f
        return numberOfSteps
    elif m == 1 and f > m:
        numberOfSteps = f - m
        return numberOfSteps
    else:
        while (isSolvable(m, f)):
            if m == 1 and f == 1:
                break
            elif m > f:
                if m > f * 100:
                    step = m // f
                    m = m - f*step
                    numberOfSteps += step
                else:
                    m = m - f
                    numberOfSteps += 1
            elif f > m:
                if f > m * 100:
                    step = f // m
                    f = f - m*step
                    numberOfSteps += step
                else:
                    f = f - m
                    numberOfSteps += 1
        # --- End While ---
        
    if m != 1 and f != 1:
        return "impossible"
    else:
        return numberOfSteps
# -=-=-= end answer function -=-=- 

# =-=-=-=-=-= "Main Function" =-=-=-=-=-=-=

endingMach = int(input().strip())
endingFacula = int(input().strip())

print(answer(endingMach, endingFacula))