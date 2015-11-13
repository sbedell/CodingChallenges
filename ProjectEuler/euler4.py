def isPalindrome(n):
    return str(n) == str(n)[::-1]

def largestPalindrome(n):
    # This only goes for 3 digit numbers
    currentLargest = 0
    for x in range(300, n):
        for y in range(300, n):
            numm = x * y
            if isPalindrome(numm):
                if numm > currentLargest:
                    currentLargest = numm
    return currentLargest

if __name__ == '__main__':
    print(isPalindrome('84348'))
    print(largestPalindrome(1000))
    #print(largestPalindrome(10))
