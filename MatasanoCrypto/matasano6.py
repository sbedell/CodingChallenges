import binascii, base64
from cryptools import singleCharXOR, splitArray, hammingDistance

# Matasano Crypto Challenges
# Challenge 6 - Break repeating-key XOR
# Totally not finished yet!

def singleCharXOR(s1, c):
    ans = str()
    for char in binascii.unhexlify(s1):
        ans += chr(c ^ char)
    return ans

def splitArray(array, n):
    return [array[i:i+n] for i in range(0, len(array), n)]


# Verify Hamming Distance:
assert(hammingDistance("this is a test", "wokka wokka!!!") == 37)

# ------- DECRYPTION -------

# 0. Unbase64'ing the text:
ciphertext = bytearray()
with open("inputData/6.txt") as f:
    for line in f:
        ciphertext += base64.b64decode(line.strip())
# print(ciphertext)

""" Logically Equivalent:
ciphertext2 = str()
with open("6.txt") as f:
    for line in f:
        ciphertext2 += line.strip()
print(base64.b64decode(ciphertext2))
print(ciphertext == base64.b64decode(ciphertext2))
"""

# 1. Trying keysizes from 2 to 40:
smallestKeysize = 3.0
for KEYSIZE in range(2, 41):
    # 3. Splitting text into KEYSIZE chunks and finding normal edit distance:
    #normEditDist = float((hammingDistance(ciphertext[:KEYSIZE].decode(), ciphertext[KEYSIZE:KEYSIZE+KEYSIZE].decode())) / KEYSIZE)
    # normEditDist = float(hammingDistance(
    if normEditDist < smallestKeysize:
        pass
        #print(normEditDist, ciphertext)
        smallestKeysize = normEditDist
print (smallestKeysize)

""" OLD SHIT
for KEYSIZE in range(2, 41):
    normEditDist = float((hammingDistance(ciphertext[:KEYSIZE].decode(), ciphertext[KEYSIZE:KEYSIZE+KEYSIZE].decode())) / KEYSIZE)
    if normEditDist == 2.0:
        print(KEYSIZE, normEditDist)

"""
