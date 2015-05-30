#!/usr/bin/py
# Head ends here

def stringSimilarity(a):
    answer = 0
    
    suffixes = stringSuffixes(a)
    for suffix in suffixes:
        count = 0
        while (count < len(suffix)):
            if suffix[count] == a[count]:
                answer = answer + 1
            else:
                break
            count = count + 1
    
    return answer

""" Returns a list of all the suffixes of the string s """
def stringSuffixes(s):
    suffixes = list() 
    
    for i in range(len(s)):
        suffixes.append(s[i:])
        
    return suffixes

    
# Tail starts here
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        a = input()
        print(stringSimilarity(a))