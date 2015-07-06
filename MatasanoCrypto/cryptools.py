import base64
import binascii
import string
import random
import os

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Text processing functions:
def splitArray(array, n):
    ''' array - an array or string to be split into a list
        n - length of the chunks
    '''
    return [array[i:i+n] for i in range(0, len(array), n)]
    
def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("String lengths are not equal")

    strSum = sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
    hexSum = sum(ch1 != ch2 for ch1, ch2 in zip(binascii.hexlify(s1.encode()), binascii.hexlify(s2.encode())))
    return strSum + hexSum

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PKCS Stuff:
# Just a custom exception, no error message values
class PaddingError(Exception):
    def __init__(self):
        pass
    
def paddingPKCS7(s, n):
    '''
    s - string to pad
    n - blocksize to pad UP TO
    '''
    amtToPad = n - len(s)
    return s + bytes([amtToPad] * amtToPad)

def validatePKCS7(bytestring):
    """
    Takes in a plaintext.
    Determintes if it has valid PKCS#7 padding
    If so, it strips the padding off and returns the plaintext
    If not, it raises an exception
    """
    lastByte = bytestring[-1]   # type = int
    
    expectedPadding = bytestring[-lastByte:]    # type = bytes
    for b in expectedPadding:
        if b != lastByte:
            raise PaddingError
    return bytestring[:-lastByte]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge 1:
def hexToBase64(hexStr):
    return base64.b64encode(binascii.unhexlify(hexStr))

# Challenge 2:
def fixedXOR(s1, s2):
    ans = str()
    for x, y in zip(binascii.unhexlify(s1), binascii.unhexlify(s2)):
        ans += chr(x ^ y)
    return ans

# Logically Equivalent:
def fixedXOR2(s1, s2):
    return "".join(chr(x ^ y) for x, y in zip(binascii.unhexlify(s1), binascii.unhexlify(s2)))

# Not Unhexlifying:
def fixedXorNoUnhex(s1, s2):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

# Challenge 3:
def singleCharXOR(s1, c):
    ans = str()
    for char in binascii.unhexlify(s1):
        ans += chr(c ^ char)
    return ans

# Challenge 4?
def freqAnalysis(file):
    wordFreq = dict()
    with open(file) as f:
        for line in f:
            for word in line.split():
                if word in wordFreq:
                    wordFreq[word.strip().strip("();,?.\"")] += 1
                else:
                    wordFreq[word.strip().strip("();,?.\"")] = 1
    words = list()
    for word in wordFreq.keys():
        if wordFreq[word] > 25:   # tune this to whatever num you want
            words.append(word.lower())
    return words

# Challenge 5:
def repeatingXOR( plaintext, key ):
    '''
    plaintext = byte encoded string
    key = byte encoded string
    '''
    crypt = str()
    iKey = 0
    for c in plaintext:
        crypt += chr(c ^ key[iKey])
        iKey = (iKey + 1) % len(key)    # increase by 1, mod by keylen
    return binascii.hexlify(crypt.encode())

# Challenge 8:
def ecbDetected(ciphertext):
    '''
    Returns true if there are repeating 16 byte chunks
    Returns false otherwise.
    ciphertext = text to check
    '''
    chunkedText = splitArray(ciphertext, 16)
    repeatedBlocks = set()
    for chunk in chunkedText:
        repeatedBlocks.add(chunk)
    return len(repeatedBlocks) < len(chunkedText)

# Garbage for challenge 6:
def getXorKeysize(ciphertext):
    # Dict to store keysizes
    keySizes = {}
    for ks in range(2, 40):
        normEditDist = float((hammingDistance(ciphertext[:ks].decode(), ciphertext[ks:ks+ks].decode())) / ks)
        if normEditDist < smallestKeySize:
            smallestKeySize = normEditDist

##def getXorKeysize2(ciphertext):
##    blocks = splitArray(ciphertext, 2)
            
def bruteXorKey():
    pass

def breakRepeatingKeyXOR():
    pass
